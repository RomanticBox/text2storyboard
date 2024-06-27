# import packages
import os
import pandas as pd
import tqdm as tqdm
import torch
import transformers
import openai
import json

from diffusers import StableDiffusionXLPipeline
from huggingface_hub import login
login(token='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')



# set parameters
openai.api_key = 'sk-proj-q8qVMtlcT0kDQhxZb1huT3BlbkFJDwhBYc6hMGBUzVyyviYk'

get_input_from_users = False # 이부분을 True로 바꾸면 사용자로부터 직접 인풋을 받음 / False로 설정시 미리 저장해둔 샘플이 자동으로 input으로 들어감
set_dir = '/root/text2storyboard/llm'

model_name = "gpt-3.5-turbo-instruct"
input_path = '/root/text2storyboard/llm/sample_inputs/sample_inputs.json'

prompt_path = '/prompts/prompts.json'
prompt_type = '1shot'

output_path = '/outputs'
output_file_name = 'response_{0}_{1}d.json'.format(model_name,prompt_type)

sdxl_model = "stabilityai/stable-diffusion-xl"
image_output_path = './generated_images/'


### STORYBOARD CAPTION GENERATION PART

def read_json(path):
    json_objects = pd.read_json(path,encoding='utf-8')
    return json_objects.to_dict('records')


# load input data
def load_input():

    print('******* Loading Input Data . . . *******')
    input_data = read_json(input_path)
    print('******* Input Data Loaded !!! *******')

    return input_data

# or get input from users (default)
def get_input():

    print('******* Plz type your story in . . . *******')
    user_input = input()
    input_data = [{'id':0,'storytelling':user_input}]
    print('******* Input Data Loaded !!! *******')

    return input_data

# load prompt file
## dtype = str
def load_prompt(input_data,prompt_type):

    print('******* Loading Prompt . . . *******')

    # read prompt json files
    path = set_dir + prompt_path
    prompts = read_json(path)
    prompt = dict(prompts[prompts[0]==prompt_type])

    # load input data
    prompt_list = []

    # gpt3 template
    if '1shot' == prompt_type:
        for input in input_data:
            template = '[system]\n{system}\n\n[user]\n{user}\n\n'.format(system = prompt['prompt'][0]['content'], user = prompt['prompt'][1]['content']+'\n'+input['storytelling'])
            prompt_list.append({ "id":input['id'], 'prompt':template })
    elif 'zeroshot' == prompt_type:
        pass
    
    print('******* Prompt Loaded !!! *******')

    return prompt_list



# generate model response
def generate_response(prompt_list,input_data):

    # llama3-8b-instruct
    print('******* Model inference Started . . . *******')  
    output = openai.Completion.create(
        model=model_name,
        prompt=prompt_list[0]['prompt'],
        temperature=0.7,
        max_tokens=100)
    
    # save responses in dictionary  
    output = output.choices[0].text.strip()
    image_caption = output.split('\n')
    response = {'storytelling' : input_data[0]['storytelling'],
                'image_caption' : image_caption,
                'sentence_num' : len(image_caption)
                }
    print('******* Model Inference Finished !!! *******\n\n')
    for i in range(response['sentence_num']):
        print(response['image_caption'][i])
    print('\n')

    return response


def asking_who(response):
    # 프롬프트 리스트 → LLM → 주요 등장인물을 알아내기 (한명만)
    # response['image_caption']
    
    #prompt_list = f"Who is the main character in {response['image_caption'][0]}? " + " Please choose only one main character." + " The main character in the story is "
    prompt_list = f"Describe in 200 words, Who is the main character in {response['image_caption'][:]}? " + " Please choose only one main character."
    # character_name = f"who is the main character in {response['image_caption'][:]}? Give me only one main character's name."

    
    output = openai.Completion.create(
        model=model_name,
        prompt=prompt_list,
        temperature=0.7,
        max_tokens=200)
    
    # character_name = openai.Completion.create(
    #     model=model_name,
    #     prompt=character_name,
    #     temperature=0.7,
    #     max_tokens=50)
    
    # character_name = character_name.choices[0].text.strip()
    output = output.choices[0].text.strip()
    return output

def making_sdxl_prompt(response):
    # 등장인물을 묘사하는 것만 LLM에 넣어서 sdxl 프롬프트를 만들어달라고 하기.
    
    prompt_list = f"Given the response: '{response}', please create an SDXL prompt based on this information."
    #prompt_list = f"Given the response: '{response}', please create an SDXL prompt based on this information in 200 words."
    # output = openai.Completion.create(
    #     model=model_name,
    #     prompt=prompt_list,
    #     temperature=0.7)
    
    output = openai.Completion.create(
        model=model_name,
        prompt=prompt_list,
        temperature=0.7,
        max_tokens=200)
    
    output = output.choices[0].text.strip()

    
    return output
    

# save file
def save_result(response):

    print('******* Saving Results . . . *******')
    path = set_dir + output_path + output_file_name
    with open(path,'w') as json_file:
        json.dump(response,json_file,indent=4)
    print('******* Result Saved in {} !!! *******'.format(path))


### SDXL IMAGE GENERATION PART

# image generation
def generate_character_sample_images(response):

    print('******* Image Generation Started *******')
    pipe = StableDiffusionXLPipeline.from_pretrained(sdxl_model).to('cuda')

    # modify this part to apply style transfer
    for idx in range(6):

        print(f'*******{idx+1}th character sample image generating . . . *******')

        img_cap = response
        img = pipe(img_cap).images[0] # 단순 llm 결과만 넣은 것 ( sks identifier 적용 X )

        img.save(image_output_path + f'character_sample{idx+1}.png')



def generate_images(response):

    print('******* Base Image Generation Started *******')
    pipe = StableDiffusionXLPipeline.from_pretrained(sdxl_model).to('cuda')

    # modify this part to apply style transfer
    for idx in range(response['sentence_num']):

        print(f'*******{idx+1}th image generating . . . *******')

        img_cap = response['image_caption'][idx][3:]
        img = pipe(img_cap).images[0] # 단순 llm 결과만 넣은 것 ( sks identifier 적용 X )

        img.save(image_output_path + f'image_{idx+1}.png')

# def cnt_main_character(response, main_character):
#     # 프롬프트 결과에서 찾은 주요 등장인물이 몇번째 문장에 등장하는지 저장하기 
#     explain = response['image_caption']
    
#     # 문장을 분리
#     sentences = explain.split('.')
    
#     # 등장하는 문장 번호를 저장할 리스트
#     sentence_numbers = []

#     # LLM에게 문장에서 주요 등장인물이 등장하는지 확인하는 작업을 요청하는 프롬프트 작성
#     for i, sentence in enumerate(sentences):
#         if sentence.strip():  # 빈 문장은 무시
#             prompt = (
#                 f"Given the sentence: \"{sentence.strip()}\" and the main character description \"{main_character}\", "
#                 "does this sentence contain the main character? Answer with 'yes' or 'no'."
#             )
            
#             # OpenAI API 호출
#             response = openai.Completion.create(
#                 model=model_name,  # 모델 이름 (적절히 변경)
#                 prompt=prompt,
#                 temperature=0.7,
#                 max_tokens=10
#             )
            
#             # LLM 응답을 확인하여 문장 번호를 저장
#             llm_response = response.choices[0].text.strip().lower()
#             if llm_response == 'yes':
#                 sentence_numbers.append(i + 1)  # 문장 번호는 1부터 시작
    
#     return sentence_numbers



def cnt_main_character(response, main_character):
    # 프롬프트 결과에서 찾은 주요 등장인물이 몇번째 문장에 등장하는지 저장하기 
    explain = response['image_caption']
    
    # 등장하는 문장 번호를 저장할 리스트
    sentence_numbers = []

    # LLM에게 문장에서 주요 등장인물이 등장하는지 확인하는 작업을 요청하는 프롬프트 작성
    for i, sentence in enumerate(explain):
        if sentence.strip():  # 빈 문장은 무시
            prompt = (
                f"Given the sentence: \"{sentence.strip()}\" and the main character \"{main_character}\", "
                "does this sentence contain the main character? Answer with 'yes' or 'no'."
            )
            
            # OpenAI API 호출
            response = openai.Completion.create(
                model=model_name,  # 모델 이름 (적절히 변경)
                prompt=prompt,
                temperature=0.7,
                max_tokens=10
            )
            
            # LLM 응답을 확인하여 문장 번호를 저장
            llm_response = response.choices[0].text.strip().lower()
            if llm_response == 'yes':
                sentence_numbers.append(i + 1)  # 문장 번호는 1부터 시작
    
    return sentence_numbers


# main
def main():
    os.chdir(set_dir)

    # STORYBOARD CAPTION GENERATION
    if get_input_from_users:
        input_data = get_input()
    else: 
        input_data = load_input()

    prompt_list = load_prompt(input_data=input_data, prompt_type=prompt_type)
    response = generate_response(prompt_list,input_data)
    #print(response)
    
    save_result(response)
    
    output = asking_who(response) # 주요 등장인물을 알아낸 결과 -> 프론트로 전달해야함
    # breakpoint()
    # output, character_name = asking_who(response)
    # print(output)
    # print(haracter_name)



    cnt_main_character_in_output = cnt_main_character(response, main_character)
    #고칠점 : token 잘리는거 고치기 -> 몇 자 이내로 해줘 ->done
    input = 'maya, who has long hair is playing with her dog' # 여기 고쳐야 함. 프론트에서 사용자한테서 입력받은 정보로 
    sdxl_prompt = making_sdxl_prompt(input)

    

    # SDXL IMAGE GENERATION PART
    generate_character_sample_images(sdxl_prompt)
    generate_images(response)



if __name__ == '__main__':
    main()
