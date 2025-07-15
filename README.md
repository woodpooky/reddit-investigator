### 🕵️ Reddit Investigator

Check any Reddit user’s comment and post history within a specific subreddit.

### Features:

    🔎 View user activity (comments + submissions) in any subreddit

    📅 See account creation date

    📊 Sort results by type or date

    🖥️ Runs locally in your browser

    ✅ OS-agnostic: works on Windows, macOS, and Linux via Docker

### Requirements:

- Docker Desktop installed
  (Ensure Docker Compose is enabled — included by default)
- Link: https://www.docker.com/ja-jp/products/docker-desktop/

### Setup: 

1. Clone the repository or download the repository zip

2. Update the config.yaml file with your own client_id and secret (API credentials) from Reddit.
    -  🔐 You can get Reddit API credentials from: https://www.reddit.com/prefs/apps and select "script" as an app type.

#### Example:


     reddit:
 
         client_id: lafkhsifhsd9ghd
         
         client_secret: lkbfSDf9sd9gsg0od9gyh0
         
         user_agent: script:reddit-checker:v1.0 (by u/YOUR_USERNAME)
     

    

#### ▶️ Running the App

1. Open Terminal/Powershell/Command Prompt and navigate to the folder.
   
       - Windows: Shift + Right-click inside a blank spot of the folder > Open Terminal / Open with powershell
       - Mac: Right-click the folder > New Terminal At Folder

3. Then run the below command:

    docker compose up --build


4. Open your browser and go to:

    http://localhost:5000

#### Usage

1. Enter the Reddit username (e.g. batman)

2. Enter the subreddit name (e.g. AskReddit)

3. Click Check Activity


   


You’ll see:

    📅 Account creation date

    📄 All posts & comments in that subreddit

    🔃 Sortable table by type and date



