import os
import shutil
import argparse

'''

    To add a new folder and its associated file types, create a new dictionary item like this:
    'folder_name': ['.file_extension1', '.file_extension2', ...]

    To modify an existing folder and its file types, update its list of extensions in the dictionary.

'''

def file_wizard(directory):
    
    file_categories = {
        'documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', '.csv', '.rtf', '.odt'],
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.psd', '.ai', '.eps', '.PNG', '.webp'],
        'videos': ['.mp4', '.mkv', '.flv', '.avi', '.mov', '.wmv', '.mpeg', '.mpg', '.webm', '.MOV'],
        'audio': ['.mp3', '.wav', '.m4a', '.flac', '.ogg', '.aac', '.wma'],
        'archives': ['.zip', '.rar', '.tar', '.gz', '.7z', '.iso', '.dmg', '.apk'],
        'programs': ['.exe', '.msi', '.dmg', '.pkg', '.deb', '.rpm'],
        'code': ['.py', '.cpp', '.h', '.html', '.css', '.js', '.java', '.rb', '.pl', '.swift', '.json', '.key', '.pem'],
        'fonts': ['.ttf', '.otf', '.woff', '.woff2'],
        # Add more folder items here as needed
    }

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file)[1]

            for category, extensions in file_categories.items():
                if file_ext in extensions:
                    category_path = os.path.join(directory, category)

                    if not os.path.exists(category_path):
                        os.makedirs(category_path)

                    shutil.move(file_path, os.path.join(category_path, file))
                    print(f"Moved {file} to {category} folder")
                    break

def main():
    parser = argparse.ArgumentParser(description='Organize files based on their file type.')
    parser.add_argument('directory', type=str, help='Directory to organize')
    args = parser.parse_args()

    file_wizard(args.directory)

if __name__ == '__main__':
    main()
