## 미완성!!!!!

# import packages
import os
import pandas as pd
import tqdm as tqdm
import torch
import transformers


# set parameters
set_dir = '/mnt/c/Users/yelin/Documents/GitHub/Ybigta_assignment/text2storyboard/llm'

model_name = "meta-llama/Meta-Llama-3-8B-Instruct"
input_path = './sample_inputs/sample_inputs.json'

prompt_path = '/prompts/prompts.json'
prompt_type = 'llama3_1shot'

output_path = '/outputs/'
output_file_name = 'response_{0}_{1}.csv'.format(model_name.split('/')[1],prompt_type)


def read_json(path):
    json_objects = pd.read_json(path,encoding='utf-8')
    return json_objects.to_dict('records')


# load input data
def load_input():

    print('******* Loading Input Data . . . *******')
    input_data = read_json(input_path)
    print('******* Input Data Loaded !!! *******')

    return input_data


# load prompt file
## dtype = str
def load_prompt(prompt_type):

    print('******* Loading Prompt . . . *******')

    # read prompt json files
    path = set_dir + prompt_path
    prompts = read_json(path)
    prompt = dict(prompts[prompts[0]==prompt_type])

    # load input data
    input_data = load_input()
    prompt_list = []

    # llama template
    if 'llama' in prompt_type:
        for input in input_data:
            template = '<|start_header_id|>system<|end_header_id|>\n\n{system}<|eot_id|>\n<|start_header_id|>user<|end_header_id|>\n\n{user}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n'.format(system = prompt['prompt'][0]['content'], user = prompt['prompt'][1]['content']+input['storytelling'])
            prompt_list.append({ "id":input['id'], 'prompt':template })
    elif 'gpt' in prompt_type:
        pass
    
    print('******* Prompt Loaded !!! *******')

    return prompt_list



# load model
def load_model(model_name,prompt_type):

    print('******* Start Loading Model . . . *******')

    # pipeline
    pipeline = transformers.pipeline(
        "text-generation",
        model = model_name,
        model_kwargs={"torch_dtype": torch.bfloat16},
        device_map="auto",
        )

    # messages & prompt
    prompt_list = load_prompt(prompt_type)
    tokenized_prompts = []
    for prompt in prompt_list:
        tokenized_prompt = pipeline.tokenizer.apply_chat_template(
            prompt,
            tokenize=False,
            add_generation_prompt=True
            )
        tokenized_prompts.append(tokenized_prompt)
    
    terminators = [pipeline.tokenizer.eos_token_id,
                   pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")]
    
    print('******* Model {} Load Finished *******'.format(model_name))

    return pipeline, tokenized_prompts, terminators


# generate model response
def generate_response(prompt_list):

    # Load Model
    pipeline, prompt, terminators = load_model(model_name,prompt_type)

    # llama3-8b-instruct
    print('******* Model inference Started . . . *******')  
    outputs = pipeline(
        prompt,
        max_new_tokens = 256,
        eos_token_id = terminators,
        do_sample =True,
        temperature = 0.6,
        top_p = 0.9)
    
    # save responses in dictionary  
    responses = []
    for i in tqdm(range(len(outputs))):
        output = outputs[i]["generated_text"][len(prompt):]
        image_caption = output.split('\n')
        response = {'id' : prompt_list[i]['id'],
                    'storytelling' : prompt_list[i]['storytelling'],
                    'image_caption' : image_caption,
                    'sentence_num' : len(image_caption)
                    }
        responses.append(response)
    print('******* Model Inference Finished !!! *******')

    return responses


# save file
def save_result(responses):

    print('******* Saving Results . . . *******')
    path = set_dir + output_path
    responses.to_csv(path, encoding='utf-8', intent=4)
    print('******* Result Saved in {} !!! *******'.format(path))


# main
def main():
    os.chdir(set_dir)
    prompt_list = load_prompt(prompt_type)
    responses = generate_response(prompt_list)
    save_result(responses)




if __name__ == '__main__':
    main()
