# FileWizard

File Wizard is a command-line tool that helps organize files based on their file type by moving them to appropriate folders. It uses Python's built-in `os` and `shutil` libraries to walk through the directory tree and identify each file's type based on its file extension. The tool then moves the file to the appropriate category folder based on the predefined `file_categories` dictionary.

## Usage

To use this tool, save the `file_wizard.py` script to your local machine and run it from the command line with the directory you want to organize as an argument:

```python file_wizard.py /path/to/your/directory```


## Customization

The `file_categories` dictionary can be customized to include additional categories and file extensions as needed. Note that the script is designed to organize files by extension, so it may not work well for files with complex or non-standard file names.

## Contributing

If you find a bug or have a feature request, please open an issue or submit a pull request. Contributions are welcome!

## License

This tool is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to modify this README file as needed for your project. You may want to include additional sections such as a description of the `file_categories` dictionary, examples of file names and extensions that are not recognized by the tool, or instructions for running the tool on different operating systems.
