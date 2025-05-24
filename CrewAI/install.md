# Installation

Modified (A.L. 2025-05-24) from https://docs.crewai.com/installation

> Get started with CrewAI - Install, configure, and build your first AI crew


## Tutorial


  **Python Version Requirements**

  CrewAI requires `Python >=3.10 and <3.13`. Here's how to check your version:

  ```bash
  python3 --version
  ```

  If you need to update Python, visit [python.org/downloads](https://python.org/downloads), 
  or check [Anaconda](https://www.anaconda.com) for a full installation of Python with friends.


CrewAI uses the `uv` as its dependency management and package handling tool. It simplifies project setup and execution, offering a seamless experience.

If you haven't installed `uv` yet, follow **step 1** to quickly get it set up on your system, else you can skip to **step 2**.

### Install `uv`
  - **On macOS/Linux:**

      Use `curl` to download the script and execute it with `sh`:

      ```shell
      curl -LsSf https://astral.sh/uv/install.sh | sh
      ```

      If your system doesn't have `curl`, you can use `wget`:

      ```shell
      wget -qO- https://astral.sh/uv/install.sh | sh
      ```

  -  **On Windows:**

      Use `irm` to download the script and `iex` to execute it:

      ```shell
      powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
      ```

      If you run into any issues, refer to [UV's installation guide](https://docs.astral.sh/uv/getting-started/installation/) for more information.


  ### Install CrewAI 🚀
  - Run the following command to install `crewai` CLI:

   ```shell
  uv tool install crewai --python=3.12
   ```
   **Check**:
       ```shell
      crewai --help
      ```  
      
If you encounter a `PATH` warning, run this command to update your shell:

  ```shell
  uv tool update-shell
   ```
    

    
If you encounter the `chroma-hnswlib==0.7.6` build error (`fatal error C1083: Cannot open include file: 'float.h'`) on Windows, install (Visual Studio Build Tools)\[[https://visualstudio.microsoft.com/downloads/](https://visualstudio.microsoft.com/downloads/)] with *Desktop development with C++*.
    

  - To verify that `crewai` is installed, run:
      ```shell
      uv tool list
      ```

    * You should see something like:
      ```shell
      crewai v0.121.0
      - crewai
      ```

    * If you need to update `crewai`, run:
      ```shell
      uv tool install crewai --upgrade
      ```

  Installation successful! You're ready to create your first crew! 🎉</Check>


### Creating a CrewAI Project

We recommend using the `YAML` template scaffolding for a structured approach to defining agents and tasks. Here's how to get started:

#### Generate Project Scaffolding
* Run the `crewai` CLI command:

```shell
crewai create crew <your_project_name>
```
This creates a new project with the following structure:

```shell
        my_project/
        ├── .gitignore
        ├── knowledge/
        ├── pyproject.toml
        ├── README.md
        ├── .env
        └── src/
            └── my_project/
                ├── __init__.py
                ├── main.py
                ├── crew.py
                ├── tools/
                │   ├── custom_tool.py
                │   └── __init__.py
                └── config/
                    ├── agents.yaml
                    └── tasks.yaml
```

- Your project will contain these essential files:

| File          | Purpose                                  |
| ------------- | ---------------------------------------- |
| `agents.yaml` | Define your AI agents and their roles    |
| `tasks.yaml`  | Set up agent tasks and workflows         |
| `.env`        | Store API keys and environment variables |
| `main.py`     | Project entry point and execution flow   |
| `crew.py`     | Crew orchestration and coordination      |
| `tools/`      | Directory for custom agent tools         |
| `knowledge/`  | Directory for knowledge base             |


- Start by editing `agents.yaml` and `tasks.yaml` to define your crew's behavior.

- Keep sensitive information like API keys in `.env`.
  

### Run your Crew
  Before you run your crew, make sure to run:
  ```bash
  crewai install
  ```
  If you need to install additional packages, use:
  ```shell
  uv add <package-name>
  ```
  To run your crew, execute the following command in the root of your project:
  ```bash
  crewai run
  ```

## Enterprise Installation Options

For teams and organizations, CrewAI offers enterprise deployment options that eliminate setup complexity:

### CrewAI Enterprise (SaaS)

  * Zero installation required - just sign up for free at [app.crewai.com](https://app.crewai.com)
  * Automatic updates and maintenance
  * Managed infrastructure and scaling
  * Build Crews with no Code

### CrewAI Factory (Self-hosted)

  * Containerized deployment for your infrastructure
  * Supports any hyperscaler including on prem depployments
  * Integration with your existing security systems


