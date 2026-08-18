   ## STEP 1:
   On Terminal:
   ```bash
   # Run 1st
   git clone https://github.com/codeprojectsndfun-design/google-form-automator.git
   # Run 2nd
   cd google-form-automator
   ``` 
   ## STEP 2: 
   **Create and activate a virtual environment (Optional but Recommended):**

   ```bash
   # On Windows
   python -m venv venv # 1. create (wait & some secs)

   .\venv\Scripts\activate # 2. Activate

   # On macOS/Linux
   python3 -m venv venv # 1. create

   source venv/bin/activate # 2.  Activate
   ```
   ## STEP 3:
   Install dependencies
   ```bash
   python -m pip install -r requirements.txt
   ``` 
   ## STEP 4:
   OPEN "config.py" and Update variables

   ## STEP 5:
   WARNING: keep all chrome windows closed from now on every step

   Run "setup_profile.py" 
   + Login in Chrome (under 120 secs) and close window
   + Saves ur profile in "/chrome_profile"
 
   ## STEP 6:
   (Clear the form if filled before by opening form link and click clear form)

   (Keep Chrome Window Closed)
   
   Run "main.py" (Solve captcha ocasionally after hitting submit)