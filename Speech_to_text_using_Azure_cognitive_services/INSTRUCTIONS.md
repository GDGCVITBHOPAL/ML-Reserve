- <h2>Setup Instructions</h2>

  - ### Base Operating System used while making this prototype (Windows 10)</br>

    Install Windows 10 and apply all updates.

  - ### Edge<br>

    Install Edge (Chromium), or any other browser

  - ### .NET Core SDK<br>

    Download and install from https://dotnet.microsoft.com/download<br>
    (download .NET Core SDK - not just the runtime)

  - ### C++ Redistributable<br>

    Download and install the Visual C++ Redistributable (x64) from https://aka.ms/vs/16/release/vc_redist.x64.exe.

  - ### Node.JS<br>

    Download the latest LTS version from https://nodejs.org/en/download/<br>
    Install using the default options

  - ### Python (and required packages)<br>

    Download version 3.8 from https://www.anaconda.com/products/individual<br>
    Run setup to install - Important: Donot select the options to add Anaconda to the PATH variable.

  - ### Python environment<br>

    After installation, open the Anaconda prompt and enter the following commands to install packages:

  - ### Code<br>

    <i>pip install flask requests python-dotenv pylint matplotlib pillow (Optional)</i><br>
    <i>pip install azure-cognitiveservices-speech==1.19.0</i>

  - ### Azure CLI<br>

    Download from https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest<br>
    Install using the default options

  - ### Git<br>

    Download and install from https://git-scm.com/download.html, using the default options

  - ### Visual Studio Code (and extensions)<br>
    Download from https://code.visualstudio.com/Download
    Install using the default options
  - ### After installation, start Visual Studio Code and on the Extensions tab (CTRL+SHIFT+X), search for and install the following extensions from Microsoft:
    - Python
    - Azure Functions
    - PowerShell
  - ### Provision a Cognitive Services Speech
    - Open the Azure portal at https://portal.azure.com, and sign is using the microsoft account linked with your Azure subscription.
    - Select **+Create Reasource** button and search for cognitive services.
    - **Subscription**: Your Azure subscription
    - **Resource group**: Choose or create a resource group
    - **Region**: Choose any available region
    - **Name**: Enter a unique name
    - **Pricing tier**: Standard S0
    - Wait for the deployement to complete
    - Copy the Key and location from **Key and Endpoint**
