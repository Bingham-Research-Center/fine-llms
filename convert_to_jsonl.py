import json

def convert_md_to_jsonl(md_file_path, jsonl_file_path):
    """
    Converts a Markdown file with Q&A pairs to a JSONL file.
    """
    with open(md_file_path, 'r') as md_file, open(jsonl_file_path, 'w') as jsonl_file:
        content = md_file.read()
        qa_pairs = content.split('---\n')
        for pair in qa_pairs:
            if pair.strip():
                lines = pair.strip().split('\n')
                question = ''
                answer = ''
                for line in lines:
                    if line.startswith('**Question:**'):
                        question = line.replace('**Question:** ', '').strip()
                    elif line.startswith('**Answer:**'):
                        answer = line.replace('**Answer:** ', '').strip()
                if question and answer:
                    json_object = {"messages": [{"role": "user", "content": question}, {"role": "assistant", "content": answer}]}
                    jsonl_file.write(json.dumps(json_object) + '\n')

if __name__ == '__main__':
    convert_md_to_jsonl('reference-text/Q-A-DRAFT.md', 'data/Q-A-DATASET-instruct.jsonl')
