import os

def load_prompt(file_name: str) -> str:
    """
    Lê o conteúdo de um arquivo de prompt e o retorna como uma string.
    """
    try:
        this_file_path = os.path.abspath(__file__)

        utils_dir = os.path.dirname(this_file_path)
        
        src_dir = os.path.dirname(utils_dir)

        base_dir = os.path.dirname(src_dir)

        prompts_dir = os.path.join(base_dir, 'prompts')

        file_path = os.path.join(prompts_dir, file_name)

        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()

    except FileNotFoundError:
        return f"Erro: Arquivo de prompt '{file_name}' não foi encontrado no caminho esperado: {file_path}"

    except Exception as e:
        return f"Ocorreu um erro inesperado ao ler o arquivo: {e}"