# file_io_example.py

def count_words_in_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            text = infile.read()
            word_count = len(text.split())
        
        with open(output_file, 'w') as outfile:
            outfile.write(f'Total words: {word_count}\n')
        
        print(f'Total words counted: {word_count}')
    except FileNotFoundError:
        print(f"The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = 'input.txt'
    output_file = 'output.txt'
    count_words_in_file(input_file, output_file)
