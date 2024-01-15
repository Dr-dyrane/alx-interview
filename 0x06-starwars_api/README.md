# Star Wars API - Characters

This script is designed to retrieve and display characters from a specific Star Wars movie using the Star Wars API. The script takes the Movie ID as a positional argument and fetches the corresponding characters list from the API.

## Prerequisites

- Node.js 10: To install, run the following commands:

  ```bash
  curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
  sudo apt-get install -y nodejs
  ```

- Semi-standard: To install, run:

  ```bash
  sudo npm install semistandard --global
  ```

- Request module: To install, run:

  ```bash
  sudo npm install request --global
  export NODE_PATH=/usr/lib/node_modules
  ```

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/Dr-dyrane/alx-interview.git
   ```

2. Navigate to the project directory:

   ```bash
   cd 0x06-starwars_api
   ```

3. Make the script executable:

   ```bash
   chmod +x 0-starwars_characters.js
   ```

4. Run the script with the desired Movie ID (e.g., 3 for "Return of the Jedi"):

   ```bash
   ./0-starwars_characters.js 3
   ```

## Example Output

```bash
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```

## Author

- **Alexander Udeogaranya** - Software Engineer at ALX Software Engineering
  - GitHub: [Dr-dyrane](https://github.com/Dr-dyrane)

Feel free to reach out for any questions or clarifications. May the force be with you! 🌌🚀
