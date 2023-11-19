### Inspiration  
Developers often find themselves switching between the terminal and a web browser to look up explanations for error messages. This repetitive task disrupts their workflow and reduces efficiency. Moreover, when looking up these error messages online, they lack the context of their entire codebase. This absence of complete context can lead to less effective solutions and a greater time investment in troubleshooting.

### What it does  
Terminal.AI is a groundbreaking devtool designed to boost developer productivity by harnessing the power of generative AI directly within the terminal. When an error is encountered, the tool actively analyzes the complete error stack, all relevant files, as well as environment variables. It then autonomously provides detailed explanations, actionable solutions, and guides the developer to the exact file and line where these solutions can be implemented. This process is seamlessly executed within the terminal environment, negating the need to exit the terminal. Additionally, Terminal.AI accepts custom prompts via the command line interface for more tailored assistance.

### How we built it  
To create Terminal.AI, we integrated various Python modules such as subprocess, glob, os, sys, and platform to capture error outputs, retrieve contents of relevant Python files, and gather environment details like the operating system and installed packages. This data is then processed using OpenAI's GPT API, which provides intelligent analysis of the errors, suggesting solutions and pinpointing their implementation locations within the code. The tool is designed for seamless operation within the terminal, enhanced with features like color-coded error messages for improved readability, and accommodates custom prompts via the command line for tailored assistance.

### Challenges we ran into  
The primary challenge was mastering prompt engineering. Crafting prompts that accurately and effectively communicate the developers' needs to the AI was crucial for the tool's effectiveness.

Accomplishments that we're proud of  
Terminal.AI is uniquely capable of understanding the complete context of a codebase while generating solutions. This comprehensive approach ensures more accurate and contextually relevant assistance.

### What we learned  
The project reinforced the immense potential of generative AI in enhancing terminal-based workflows. It opens new avenues for AI application in software development and in developer productivity.

What's next for Terminal.AI  
Our next step is to integrate Terminal.AI with GitHub history. This will allow the AI to consider recent changes made in the repository, providing even more contextual and relevant solutions based on the evolving state of the codebase.

# How to run

1. Download Package
   
   ```bash
   pip install mhacks1

2. Run Your Project
   
   ```bash
   mhacks /filePath
