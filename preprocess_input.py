# import os
# def preprocess_input(input_file):
#     output_file = f"{os.path.splitext(input_file)[0]}_cleaned.txt"
    
#     with open(input_file, 'r', encoding='utf-8') as f:
#         with open(output_file, 'w', encoding='utf-8') as f_out:
#             for line in f:
#                 line = line.strip()
#                 if line.startswith('HEADING'):
#                     continue  # Skip lines that start with 'HEADING'
#                 f_out.write(line + '\n')

# input_file = '12.txt'
# preprocess_input(input_file)

import os
os.makedirs('text_output', exist_ok=True)

def concatenate_files(input_folder='raw_txt', output_folder='text_output'):
    output_file = os.path.join(output_folder, 'concatenated.txt')
    with open(output_file, 'w', encoding='utf-8') as f_out:
        for file in os.listdir(input_folder):
            with open(os.path.join(input_folder, file), 'r', encoding='utf-8') as f:
                f_out.write(f.read() + '\n')

concatenate_files()