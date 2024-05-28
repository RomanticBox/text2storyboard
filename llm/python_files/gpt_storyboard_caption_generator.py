# import packages
import os
import pandas as pd
import tqdm as tqdm
import torch
import transformers
import openai
import json
openai.api_key = 'sk-proj-q8qVMtlcT0kDQhxZb1huT3BlbkFJDwhBYc6hMGBUzVyyviYk'


# set parameters
get_input_from_users = False # 이부분을 True로 바꾸면 사용자로부터 직접 인풋을 받음 / False로 설정시 미리 저장해둔 샘플이 자동으로 input으로 들어감
set_dir = '/mnt/c/Users/yelin/Documents/GitHub/Ybigta_assignment/text2storyboard/llm'

model_name = "gpt-3.5-turbo-instruct"
input_path = './sample_inputs/sample_inputs.json'

prompt_path = '/prompts/prompts.json'
prompt_type = '1shot'

output_path = '/outputs/'
output_file_name = 'response_{0}_{1}.json'.format(model_name,prompt_type)


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


# save file
def save_result(response):

    print('******* Saving Results . . . *******')
    path = set_dir + output_path + output_file_name
    with open(path,'w') as json_file:
        json.dump(response,json_file,indent=4)
    print('******* Result Saved in {} !!! *******'.format(path))


# main
def main():
    os.chdir(set_dir)

    if get_input_from_users:
        input_data = get_input()
    else: 
        input_data = load_input()

    prompt_list = load_prompt(input_data=input_data,prompt_type=prompt_type)
    response = generate_response(prompt_list,input_data)

    save_result(response)




if __name__ == '__main__':
    main()
