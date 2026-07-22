

def read_file(file_path,repo_path):
    content = file_path.read_text(encoding="utf-8")
    
    relative_path = file_path.relative_to(repo_path)
    
    
    file_data={
        "file_path" :  relative_path.as_posix(),
        "extension" :file_path.suffix.lower(),
        "content"   :content
        
    }
    
    return file_data



