# Instagram Non-Followers Analysis

This Python script uses the `instaloader` library to analyze an Instagram profile's followers and following lists. It identifies accounts that the user follows but do not follow back. Additionally, it categorizes verified and non-verified non-followers.

## Features

- Logs into an Instagram account.
- Retrieves the followers and following lists of a specified target account.
- Identifies accounts that do not follow back.
- Separates non-followers into verified and non-verified categories.
- Displays the results in the console.

## Requirements

- Python 3.x
- `instaloader` library

## Installation

1. **Clone the repository or download the script:**
   ```bash
   git clone https://github.com/yourusername/instagram-non-followers-analysis.git
   cd instagram-non-followers-analysis

2. **Install the required library:**
    ```bash
    pip install instaloader
    
## Usage

1. Run the script:

    ```bash
    python insta.py

2. Enter your Instagram credentials when prompted:

    ```mathematica
    Enter your username: your_username
    Enter your password: your_password
    Enter the target account username: target_profile_username

3. If two-factor authentication (2FA) is enabled on your account, enter the 2FA code when prompted.

4. Wait while the script gathers data and displays the results
