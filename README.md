<h1 align="center" id = "introduction">
     <a href="https://kingsland-design.herokuapp.com/" target="_blank"><img src="media/kingsland-5.jpg" alt="Blank!"/></a>
     Project Kingsland
</h1>

<h2 align="center">
    <a href="https://kingsland-design.herokuapp.com/" target="_blank">Kingsland Website</a>
</h2>

<div>
*Kingsland Design*, a website to provide logo design services.
<br>
The site is to help the user be able to provide an idea of what kind of logo they are considering and depending on the type of package these are created and uploaded for the customer to download.

This is the fourth project of a four module Full Stack Developer course provided by the [Code Institute](https://codeinstitute.net/).
Main requirements are to build a full stack site to help users manage a common dataset using HTML, CSS, JavaScript, Python+Django, Relational database (recommending MySQL or Postgres), Stripe payments and any additional libraries and API’s.
Value provisions:
1. By authenticating on the site and paying for some of its services, users can advance their own goals. Before authenticating, the site makes it clear how those goals
would be furthered by the site.
2. The site owner is able to make money by providing this set of services to the users.There is no way for a regular user to bypass the site's mechanisms and derive all of
the value available to paid users without paying.
</div>

## Contents
1. [UX](#UX)
    - [Aims](#Aims)
    - [Demographic](#Demographic-both-current-and-potential)
    - [User Stories](#User-stories)
        - [Browsers](#Browsers)
        - [Customers](#Customers)
        - [Designer](#Designer)
        - [Web developer](#Web-Developer)
    - [Development](#Development-Plan)
        - [Strategy](#Strategy)
            - [Demographic](#Demographic)
            - [Audience](#Understanding-the-audience)
            - [Requirements](#User-requirements)
            - [Importance levels](#Levels-of-importance)
        - [Design and Scope](#Design-and-Scope)
            - [Influence](#Influence)
            - [Imagery](#Imagery)
            - [Pages](#Page-sections)
            - [Structure](#Structure)
    - [Wireframe](#Wireframe)
2. [Features](#Features)
    - [Django Framework](#Django-Framework)
    - [Database](#Database)
    - [Django Connection](#Django-connection-with-AWS-S3-bucket)
    - [Consistency](#Consistency)
    - [Home](#Home-page)
    - [Login](#Login-page)
    - [Registration](#Registration-page)
    - [Profile](#Profile-page)
    - [Order Details](#Order-Details)
    - [Bag](#Bag)
    - [Information and Contact](#Contact-page)
    - [Case Studies](#Case-Studies-page)
    - [Checkout](#Checkout)
3. [Technologies Used](#Technologies-Used)
4. [Testing](#Testing) / [Test detail file](https://github.com/TezBaydu/Milestone-project-4-GraphicDesign/blob/main/TEST.md)
    - [Commits](#Commits)
    - [Code testing](#Code-testing)
    - [Element testing](#Element-testing)
    - [Device testing](#Device-testing)
    - [Colour blindness Testing](#Colour-blindness-testing)
    - [Browser testing](#Browser-testing)
    - [User testing](#User-testing)
5. [Deployment](#Deployment)
    - [Gitpod commits](#Gitpod-to-GitHub-commits)
    - [Deploying via GitHub Pages or Heroku](#Deploying-via-GitHub-Pages-/-Heroku)
        - [Heroku deployment](#Heroku-deployment)
        - [Emails](#Emails)
        - [GitHub deployment](#GitHub-deployment)
    - [Forking](#Forking-repository)
    - [Cloning](#Cloning-a-repository)
6. [Django Design](#Django-responsive-design)
7. [Stripe](#Stripe)
8. [Tips and Reminders](#Tips-and-Reminders)
9. [Bugs and Issues](#Bugs-and-Issues)
6. [Credits and Acknowledgements](#Credits-and-Acknowledgements)

***
![Responsiveness](media/kingsland-responsive.JPG)
***

## UX

### Aims

1. Clear understanding of site and business service with interactive features.

2. Easy navigation.

3. Responsive to all screens, sizes and browsers.

4. Comfortable understanding of data storage capability.

5. Safe and Secure payment function

6. Database management allowing for create, read, update and delete capability.

### Demographic both current and potential

* Businesses looking for logo design ideas.
* Users who want to have a place to store/log their purchases and order history.
* Intermediary businesses utilising the service to sell onto other businesses.
* Developers.

### User stories

#### Browsers
The user is wanting to design ideas for logos.
*   This user wants to:
1. Be able to navigate through the website easily.
2. Easily view designs and case studies of design impact.
3. Be able to navigate to relevant social links.
4. Be able to make contact for queries.

#### Customers
The user is wanting to make a purchase to obtain a business logo
*   This user wants to:
1. Be able to navigate through the website easily.
2. Easily view designs and case studies of design impact.
3. Be able to navigate to relevant social links.
4. Be able to make contact for queries.
5. Be able to create a profile which is editable.
6. Be able to view order history.

#### Designer
This user is the site owner (or could be employed by the site owner to produce logo designs)
* The user wants to:
1. Receive notification of orders with purchase confirmation.
2. Have some detail on what is being requested to be designed.
3. Be able to receive notification of contact queries directly from website.
4. Be able to identify orders from a user to action.

#### Web Developer
This user is looking for imagery or influence for another project.

* They want to be able to:
1. Have easy navigation.
2. Be able to make contact with Developer/Site Owner.
3. Have an opportunity to clone site if wanting to use content.
4. Option to access repository if authorised

[Back to top ⇧](#introduction)

### Development Plan
Development decisions based on user story capabilities in line with interactivity with a database (AWS).

[Back to top ⇧](#introduction)

#### Strategy
Identifying target audience.

##### Demographic
1. People wanting to have a logo designed
    * 25-60 years old
    * Business Owners
    * Intermediary businesses making purchase and acting as a service provider on behalf of businesses
2. Web developers
    * 4th stage students with basic HTML, CSS, Javascript, JQuery, Python+Django, AWS knowledge


##### Understanding the audience
1. Personality
    * Business owners
        - Start up businesses
        - Businesses who want a change in logo design   
    * Creatives
        - Designers wanting inspiration or ideas  
2. Lifestyle
    * Earnings variable.
    * Small, Medium and large businesses

##### User requirements
1. User
    * Search site for case studies.
    * Understand service steps.
    * Register or login to profile.
    * Able to view an order from their profile.
    * Make contact directly or through social sites.

2. Developer
    * Develop online presence through interactive actions on website.
    * Provide logo design ideas.
    * Receive notifications of orders.

##### Levels of importance
Below are areas considered for levels of importance and viability

<u>Importance</u>
1. High
    * Online presence
    * Imagery
    * Interactivity
    * Contact portal
    * Profile registration and logging
    * Sales
    * Order administration function
    * Package administration function
2. Medium
    * Links to social sites
3. Low
    * Search function

<u>Viability</u>
1. High
    * Imagery.
    * Links to social sites
    * Interactivity
    * Sales
    * Package administration function
    * Order administration function
2. Medium
    * Contact portal
    * Profile registration and logging
3. Low
    * Online presence
    * Search function

[Back to top ⇧](#introduction)

### Design and Scope

#### Influence
1. A couple of friends who are graphic designers.
2. Image of logo from 1st Milestone project (Council Culture):
    * ![Council Culture](media/cc-1.jpg)

#### Imagery
1. Colours
    *   Contrasting colours for better imagery effect.
2. Imagery
    * Associations to:
        * Creativity
        * Business
        * Modern style with no curving corners of buttons or images unless necessary

#### Page sections
1. Home
2. Login
3. Registration
4. Profile
5. Contact
    * includes steps of purchase guide
6. Case Studies
7. Packages
8. Packages Details
9. Add Package
    * Admin only
10. Edit Package
    * Admin only
11. Bag
12. Checkout
13. Checkout Success and Order details
14. Profile  with order history summary
*  Potential pages to develop
    1. Other services
        - Stationary
        - Website design
        - Clothes printing
        - Payment function using Google / ApplePay


#### Structure

Hierarchical structure design for easy user navigation dependant on whether they are or are not registered.
Data schema from django-extensions used to produce data model and site associations.
[django-extansions Graph Modelling](https://django-extensions.readthedocs.io/en/latest/graph_models.html)
![Site Structure](media/data_schema.png)

[Back to top ⇧](#introduction)



### Wireframe

- Designed in [Figma](https://www.figma.com/files/team/1036770792444594249/milestone-project-4-graphicdesign?fuid=936699399740643630)

- Desktop version
![Desktop wireframe](media/wireframe-desktop.JPG)

- Mobile version
![Mobile wireframe](media/wireframe-mobile.JPG)



[Back to top ⇧](#introduction)

## Features
This site has several pages for user to easily identify section associated. Navigation menu dependancy on user being or not being registered. Front end association to back end database and back end association to website for Designer/Developer.

### Django Framework
- pip (stands for pip install packages) can be used in all kinds of tools within gitpod workspaces. This is used to install the Django framework into this workspace by typing "pip3 install django" into the Terminal. Note pip3 is installing Django for python version 3 and django 3.2.9 used for this project.
- To create a project "django-admin startproject kingsland_design ." was pushed from the terminal
    - This creates project in the current directory with files:
        * __init__.py - Directory to which files can be imported from
        * settings.py - Contains global setting for django project including which database to connect to
        * urls.py - Contains routing informatyion to type a specific url into address bar and will trigger python function
        * wsgi.py - Contains code to connect python with webserver application
- Migrations
    * code used for migrations into django admin: "python3 manage.py makemigrations
    * code used to migrate "python3 manage.py migrate

- Superuser / admin creation
    * code to create an admin / superuser: "python3 manage.py createsuperuser" and then supplying a username, email address and a password
    * Admin access allows view of all django admin sites, emails, groups, orders, social accounts, etc .... in effect all apps imported from [django allauth documentation](https://django-allauth.readthedocs.io/en/latest/installation.html)

- Application Templates
    * These can be installed via settings.py to bring in various templates created in Django.
    * This project uses user authenticaiton and model backend uploads for superusers.

- Django allauth
    * Install command: pip3 install django-allauth
    * provides apps for allowing user logins either directly or via social media sites for this project. It can also allow for easier payment, e.g. apple or google pay to make user experience smoother. This has been installed but not utilised for this project.

- Email authentication
    Allauth account allows for email verification but as created using superuser the verification has to be done via admin account in django.

### [Database](AWS)
- AWS Amazon used to store data under database name "kingsland-design"
    * Collections to store specific static data:
- Create AWS account
- go to aws.amazon.com
- select AWS management console
- Apply S3 bucket
    - Create a new bucket used to store files
    - name same as heroku app
    - allow public access and acknowledge current settings.
    - create bucket
    - within bucket go to properties and enable static website hosting applying a random site url
    - Then go to permissions tab and set up a CORS configuration to set up connection between heroku app and the bucket
        - Apply this code:
        * [
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
    ]

    - Then go to Bucket Policy and select policy generator to setup a security policy for the bucket.
    - Policy type is S3 Bucket Policy
    - In principal get all by inputting *
    - in Actions select Get Object
    - then copy the Amazon Resource Name (ARN) from S3 and apply to policy generator
    - Press Add Statement then generate policy and copy onto Bucket Policy in S3
        * apply /* on end of Resource name to allow access to all respiurces in the bucket
    - Go to Access Control list, enable ACL access so is editable and check list objects for Everyone

- Create Group, Access Policy and assign user for bucket access
    - Access Identity and Access MAnagement (IAM)
    - Create Group
        - Select User Group
        - Name the group associated to appropriate bucket as reference
        - Create Group
    - Create Policy
        - Select Policies
        - Select Create Policy and navigate to JSON tab
        - Select Import Managed Policy for pre-built access to S3
        - Search for S3 and select AmazonS3FullAccesss Policy and Import
        - Obtain the bucket ARM from S3
        - Paste after Resource in this format: "Resource": [
                "arn:aws:s3:::kingsland-design",
                "arn:aws:s3:::kingsland-design/*"
                ]
            -   The /* adds another rule for all files/folders in the bucket
        - Click Next to review Policy, name it and select Create Policy. This can now be attached to the group.
    - Create User
        - Apply appropriate uername: i.e. "project"-staticfiles-user, give programmatic access and select Next.
            - You can now apply User to the group
            - Ensure to download and save csv file to obtain keys to apply to django app
    - Once applied Django can now be connected to it.

    - Applying Media files
        - In settings remeber to cache settings with a date in the distant future so browsers can store cache for a long time and improve performance for users.
        - ensure to commit
        - In S3 media files can now be obtained directly there.
        - Go to S3 in objects overview and create folder called media
        - Then click upload and then Add media, select your files and the Next
        - Under Manage Public Permissions - Grant public access to these objects, Next and then upload
        - Images should now be viewable in your heroku application

### Django connection with AWS S3 bucket
- In Gitpod workspace install
    * pip3 install boto3
    * pip3 install django-storages
- then freeze into requirements.txt so they are also stored in heroku upon deployment
- then apply 'storage' to INSTALLED_APPS in settings
- then update settings with way to access keys through the os.environ.
- With csv download obtain keys to update heroku in config vars using same naming conventions as settings
    - also set the USE_AWS in config vars as True to know to use the AWS configuration when deployed to Heroku.
- If you have DISABLE STATIC, delete this in config vars so this can be obtained now from S3.
- Create a custom_storages.py and apply command code to apply static files into appropriate named folders (i.e. static and media)
- Once applied committing to github will push an automatic deployment to Heroku.

### Consistency

- Design with navigation menu placed in the same position at top.
    * Fixed position for consistent access.
    * A logo which leads the user back to 'Home' when clicked.
    * To have associated selections dependant on user being registered or non-registered.
    * Links to associated pages.

- Logo linking to home page in every page.

- Footer with links to social media and logo linking to Home page.

- Consistent font:
    * Poppins
    * Inter
    * to use additional in case Poppins or Inter isn't available for users:
        * Arial & sans serif

- Colours (although may vary to suit):
    * black
        * #000000 / #000 / hsl(0,0%,0%) / rgb(0,0,0)
    * midnight blue
        * #252060 / #226 / hsl(244,50%,25%) / rgb(37,32,96)
    * snow / white
        * #fffcff / #fff / hsl(300,100%,99%) / rgb(255,252,255)
    * steel teal / slategray
        * #668586 / #688 / hsl(181,13%,46%) / rgb(102,133,134)
    * ochre / chocolate
        * #dc7000 / #e70 / hsl(30,100%,43%) / rgb(220,112,0)

- Back to top button when scrolling passed top point

*![Kingsland Palette](media/kingsland-colours.png)

[Back to top ⇧](#introduction)

### Home page
1. Hero image
2. Synopsis
    - Description of service on offer.
3. Navigation menu
    - Leading non-member to
        * Login
        * Register
        * Case Studies
        * Packages
        * Contact
    - Leading member to
        * Case Studies
        * Packages
        * Contact
        * Profile
        * Sign Out
    - Leading Admin to
        * Package Management
        * Case Studies
        * Packages
        * Contact
        * Profile
        * Sign Out
4. Projects
    - Images of previous projects displayed
        * These lead to case studies page when selected
5. Testimonials
    - List of testimonials of previous projects


### Login page
1. Hero image

2. Input fields
    - Email
    - Password

3. Forgotten password link
    - Ability to have password reset option
    - If email is recognised a link is sent to email with temporary password set to be used

4. Login button
    - Data read by database and if correct allows user access
    - If incorrect a warning is flashed to state email or password is incorrect

5. If in wrong section, description to direct to registration.

6. If already logged in this option is to not be available in Navigation menu.


[Back to top ⇧](#introduction)

### Registration page
1. Hero image

2. Input fields.
    - Email - Displayed twice for confirmation
    - Username
    - Password - Displayed twice for confirmation

3. Register button if details correct.
    - Data is passed through to Admin Database

4. Warning if detail format incorrect.

5. If already registered, warning to state so and to direct user to Login page.


### Profile page
1. For members logged in only, non members will not be able to view.

2. Welcome message popup.

3. Profile details - associated to database.
    - Edit profile details function

4. Orders - associated to database.
    - Historic orders
        * Summary of orders
    - Ability to create a new order

### Order Details
1. For members logged in only, non members will not be able to view.

2. Welcome flash message.

3. Orders - associated to database.
    - Historic orders
        * shows detail of requests

4. Orders to still show even for inactive packages


### Bag
1. Packages obtained selection

2. Stored in Bag throughout site

3. Ability to checkout from within Bag anywhere in site

[Back to top ⇧](#introduction)
    
### Contact page
1. Hero-image

2. Steps on how to use service

3. Contact section
    - Full name
    - Email
    - Message
    - Submit button

4. Email to Developer/Designer and Customer Auto Reply with appropriate message.


### Case Studies page
1. Leads from images selected in Home Page

2. Images of logo associations to company

3. Description of how each were designed

4. Option to create order


### Checkout
1. Hero image
    - highlighting safe and secure purchase

2. Confirmation of order package being purchased
    - Option to select another package if incorrect

3. Form to obtain payment details
    - Submit button to lead to Stripe payment process

4. Logo request details obtained detailing requirements

[Back to top ⇧](#introduction)

## Technologies Used

- HTML5
    * Code used to provide content to the website

- CSS3
    * Code used to style content

- Javascript
    * Code used to provide interactive attributes

- [JQuery](https://code.jquery.com)
    * Code used to provide interactive attributes

- [Python](https://www.python.org)
    * Code used to provide interactive attributes

- Django
    * A high level web framework used to encourage rapid development and pragmatic design

- [AWS-Amazon Web Service](https://aws.amazon.com/)

- [Heroku](https://www.heroku.com)

- [Coolors - colour collage](https://coolors.co)

- [Picjumbo](https://picjumbo.com)

- [Unsplash](https://unsplash.com/)

- [Github](https://github.com)

- [Gitpod](https://www.gitpod.io)

- [Bootstrap v4.4](https://getbootstrap.com)

- [MDBootstrap version 4](https://mdbootstrap.com)

- [Google fonts](https://fonts.google.com)

- [Figma](https://www.figma.com/files/team/1036770792444594249/milestone-project-4-graphicdesign?fuid=936699399740643630)

- [Random Key Generator](https://randomkeygen.com)

- [Font Awesome](https://fontawesome.com)

- [Bootstrapcdn](https://www.bootstrapcdn.com)

- [Temp email site](https://temp-mail.org/en/)

- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x)

- [cdnjs](https://cdnjs.com)

- [Codepen](https://codepen.io)

- [multi-mockup](https://techsini.com/multi-mockup/index.php)

- [HTML code checker](https://validator.w3.org)

- [CSS code checker](https://jigsaw.w3.org/css-validator)

- [JS Hint JavaScript validator](https://jshint.com/)

- [PEP8](http://pep8online.com/)
 * Used to verification otherwise flake8 utilised to identify errors

- [Gif Compessor](https://www.freeconvert.com/gif-compressor)

- [RGBlind chrome extension]

- [Eye Dropper extension]

[Back to top ⇧](#introduction)


## Testing 
-   ### View [TEST.md file](https://github.com/TezBaydu/Milestone-project-4-GraphicDesign/blob/main/TEST.md)

### Commits

- Over 175 commits

### Code Testing
- HTML 
- CSS
- JavaScript
- JQuery
- Python

### Element testing
- Ensure elements behave as expected
   
### Device testing

- [multi-mockup](https://techsini.com/multi-mockup/index.php)

### Colour blindness testing

- RGBlind Chrome extensions

### Browser testing

- Chrome
- Firefox
- Microsoft Edge
- Safari

### User Testing

- Friends & Family testing

[Back to top ⇧](#introduction)

## Deployment

### Gitpod to GitHub commits

To help with controlling versions you can commit to GitHub via Gitpod.
Once you are able to view the repository in Gitpod this is done by:

1. Access the control terminal
    - Usually found at bottom of project in "workspace" section.
2. Next to gitpod/workspace/(name of project)
    - Type "git add (and name of document you wish to commit to GitHub)".
    - If you want to find all that could be committed then you can type "git add ."
3. Type "git status"
    - This will help show what files have been modified, added or deleted for a pre-check prior to committing.
4. Type "git commit -m ("and then a brief description of latest updates in quotation marks")"
5. Type "git push"
6. Log into GitHub
    - Locate repository
    - You should be able to see the latest and history of commits in code section at top right of table of files list.
    * ![git-commits](media/kingsland-design-commits.JPG)

### Deploying via GitHub Pages / Heroku

#### Heroku dependancies

- In order to deploy to Heroku initial files need to be set up to run the app.
    1. Applications
        * requirements.txt-  Lists the requirements to deploy
        * Procfile (capital P)

#### Heroku deployment

- An account will need to be registered with Heroku to deploy projects and create applications.To begin deployment:
    1. Once registered you can select "Create new app".
    2. Provide a unique app name in all lowercase letters but individual words are to be separated with a "-" and no spaces.
    3. Select region closest to you, in this case Europe.
    4. Resources tab, within add-ons search for Heroku Postgres.
        - Hobby Dev - Free version used in this instance
    5. To use this Postgres gitpod workspace will need two installations:
        - pip3 install dj_database_url
        - pip3 install psycopg2-binary
        * then freeze requirements: pip3 freeze > requirements.txt
    6. Then in gitpod workspace settings.py
        - import dj_database_url
        - Comment DATABASES default configuration
        - Replace DATABSES CONFIGURATION WITH
            * 'default': dj_database_url.parse(""Apply database url from heroku within Settings-Config Vars"")
            * or apply settings if statement to pull the DATABASE_URL, else to use the db.sqlite3 option
            - ensure to pip3 install gunicorn to act as webserver and pip3 freeze > requirements.txt in terminal.
    7. This should now allow saves and migrations to Heroku
        - This will be visible by applying the code python3 manage.py showmigrations in the terminal and all will be in-marked.
        - At this point apply python3 manage.py migrate to have all migrations set up
    8. Fixtures/Database loading/transfer
        - If you have fixtures, these can also be loaded into Heroku also by applying codes.
            * Ensure companies.json is applied prior to projects.json
            python3 manage.py loaddata companies / projects / packages
        - If you don't have fixtures and have updated directly into another database following the below code can help to import relational data
            1. Make sure your manage.py file is connected to your mysql database
            2. Use this command to backup your current database and load it into a db.json file: python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json
            3. Connect your manage.py file to your postgres database
            4. Then use this command to load your data from the db.json file into postgres: python3 manage.py loaddata db.json
    9. Create superuser to login
        - python3 manage.py createsuperuser / heroku run python3 manage.py createsuperuser to run it locally
    10. Create a Procfile to let django know gunicorn is to be used as the webserver app.
    11. In terminal login to heroku
        * heroku login -i and apply login and password details for heroku
    12. Disable Static files when deploying by:
        * heroku config:set DISABLE_COLLECTSTATIC=1 --app kingsland-design (-app kingsland-design part applied if heroku has more than one app)
    13. Apply hostname in ALLOWED_HOSTS in settings.py
        - Also apply localhost so can be stored in local host too
    14. To push to heroku
        - Initialise git connection
            * heroku git:remote -a kingsland-design
        - push to heroku
            * git push heroku master (This may not work - however please follow the next steps as deploying in github will allow commits to heroku too)
    16. Automatic deployment can be done via the GitHub repository where this project is stored.
        - Select connect to GitHub button and when pressed make sure your GitHub profile is displayed and then add your repository name in "repo-name" field and click search.
        - Once the repository is found, click "Connect" to connect to this app.
        - For thie project press "ENABLE AUTOMATIC DEPLOYS" 
        - Select "Settings".
        - Select "Reveal Config Vars".
        - Sections within env.py file are added to this section.
        - WARNING: Ensure requirements.txt & Procfile are added to repository prior to Heroku deployment or Heroku will not see these when connecting.
        - Within Heroku you should now be able to safely press the "Enable Automatic Deploys" button. Select Deploy section to view.
        - Select "ENABLE AUTOMATIC DEPLOYS".
        - Select "Deploy Branch" after selecting which version you wish to deploy. Then Wait for Heroku to load all files.
        - Once done you should see "Your app was successfully deployed" and a "View" button.
        - Select "View" button to launch the app.
        - As this is connected to GitHub, Heroku will obtain changes when these are pushed to the GitHub repository.

### Emails
- Emails to be sent have been utilised via gmail.
- Keys applied to Heroku deployment config vars and settings updated to point to this area

### GitHub deployment
- Not attempted for this site but referenced here in case required for future reference

1. Log into GitHub and look for [https://github.com/TezBaydu/Milestone-project-4-GraphicDesign] or create an account.
2. Click on settings and ensure repository name is selected to Milestone-project-4-GraphicDesign.
3. Select 'Pages' in menu section and ensure Branch is 'Master' and folder is 'root'.
4. Click save and wait for site to be published.
5. Click link in GitHub Pages section to view published site.

### Forking repository

Forking a repository in GitHub is used to make a copy of a repository which you do not have rights access to. Once you have forked a repository you will be able to make changes without affecting the original. It can also be used to suggest changes of an original project and/or propose a project as starting point.

Steps on Forking a repository:
1. Log into GitHub and look for [https://github.com/TezBaydu/Milestone-project-4-GraphicDesign] or create an account.
2. At the top right hand corner of the page select "Fork".
3. You should now have a copy of the original repository to work with on your account without affecting the original.

### Cloning a repository

Cloning a repository in GitHub allows you to make a copy of your own repository which will affect the original repository.
If you wish to make changes which do not affect the original then this should be forked.

Steps to Clone a repository
1. Log into GitHub and look for [https://github.com/TezBaydu/Milestone-project-4-GraphicDesign] or create an account.
2. Ensure "Code" has been selected in menu.
3. Select code on top right of table.
4. Select either HTTPS, SSH or CLI.
5. You can either download ZIP for static files and utilise in GitHub or open with GitHub desktop.
6. If opening with GitHub Desktop then select. If not downloaded this will need to be to utilise benefits.
7. Once opened with GitHub Desktop select "File".
8. Select "Clone repository".
9. Select GitHub and the name of the GitHub repository. (URL can also be selected and the URL applied)
10. Select repository from the sources.
11. Click "Choose".
12. Click "Clone".

For further help and info you can select [Cloning and Forking repositories](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/cloning-and-forking-repositories-from-github-desktop)

[Back to top ⇧](#introduction)

# Django responsive design
- django-responsive2 0.1.3 installed for responsive s=designs using django
    * pip3 install django-responsive2
[django-responsive2](https://django-responsive2.readthedocs.io/en/latest/readme.html#)
    * Applied and adjusted into settings but responsive adjustment not required for this project

# Stripe
* Stripe is a digital platform to allow for payments on eCommerce stores
    * JS code is applied to base.html to allow for Stripes fraud detection features
    * API Keys STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY and STRIPE_WH_KEY - required and are applied in Gitpod and/or Heroku (production-deployment) workspace variables.
        - Note when using Test-Stripe and applying endpoint url's Stripe will only work with one endpoint associated to a single source, even if it has differing url's so one has to be used at a time. Currently this is associated to the heroku endopint url as is in production


# Tips and Reminders
- CTRL / Command and Left-click on code will pull user into required file

- css not showing images
    * When this occurs, ensure cache is cleared as a pimary check: windows ctrl-f5 / has since changed and is now CTRL + SHIFT + R all pressed together.

- To create through Django
    * in terminal type: python3 manage.py startapp (name of folder)
    * add into settings.py of main project name

- JSON migrations: Best to plan what is to be migrated in advance. This to save the deletion of JSON files and migrations and starting over as I had not updated descriptions for companies:
    * Done by
        1. Delete all files from Companies and Projects in Admin
        2. Delete db.sqlite3 file in DATABASE.md
        3. Delete all files in migrations folder except __init__.py
        4. Ensure you update JSON files, views.py, models.py and admin.py prior to actions below
        5. python3 manage.py makemigrations --dry-run: This is useful to see if there are any requirements i.e. install pillow for images.
        if ok
        6. python3 manage.py makemigrations
        if ok
        7. python3 manage.py migrate --plan: This is useful to see and make sure you are only migrating app in particular, otherwise state the file after to ensure this is the only one captured.
        if ok
        8. python3 manage.py migrate (name of file if applicable)
        9. python3 manage.py loaddata companies.json and then projects.json
    * superuser will also be deleted so you will need to re-create the superuser
        1. python3 manage.py createsuperuser

- Session detail delete
    - To delete data as part of testing this can be done by selecting:
        * right click screen
        * click inspect
        * select Application
        * select Cookies
        * Right click session ID
        * select delete
    - To delete storage from site datae
        * right click screen
        * click inspect
        * select Application
        * select Storage
        * right hand pane select 'Clear site data'

- [Deleting migrations](https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html)

- Stripe Error 404
    - Resolved by making PORT 8000 Public so Stripe is able to connect

# Bugs & Issues
- django install
    When installing django, ensure it is done using command pips install django==3.2.9, django 3.4 version isn't applicable to **KWARGS.
    * Due to Gitpod update a new Gitpod Full Template has been produced to use and needs to be updated by following below. This is being done prior to deploymant or code testing.
    1. From the project directory, run this command:  curl https://raw.githubusercontent.com/Code-Institute-Org/gitpod-full-template/main/.gitpod.dockerfile > .gitpod.dockerfile  which will overwrite the old Dockerfile with the working one.
    2. Open your corrupted requirements.txt file in Gitpod, select and copy the contents.
    3. Visit https://lechien73.github.io/reqfix/ and paste in the corrupted requirements file. Click Submit
    4. In the results panel, copy the cleaned requirements and paste them into your requirements.txt file back in Gitpod and save.
    5. Add, commit and push everything to your GitHub repository.
    6. Re-create the workspace by clicking on the Gitpod button from your repository.
    7. Re-create env.py file into new workspace.
    8. Re-install packages from requirements.txt: pip3 install -r requirements.txt
    9. As database is new due to a new workspace migrations (python3 manage.py makemigrations and python3 manage.py migrate), superuser (python3 manage.py createsuperuser) and fixtures (python3 manage.py loaddata companies.json and then projects.json and packages.json) will need will need to be recreated / reloaded
    10. To note: old workspace:  https://crimson-cephalopod-9658p8le.ws-eu27.gitpod.io/
    11. New Workspace: [https://tezbaydu-milestoneprojec-srk0365muon.ws-eu27.gitpod.io/]
    12. If using gitpod variables Commit and send another request in checkout
    * Credit to Jim Morel - Code Institute Community Executive - Posted in Code Institute slack channel 7th Dec 2021

- Stripe payment succeeded test webhook
    - This will always show as error in Stripe, if this occurs at checkout there is a coding issue however this has passed the checkout test.
    - payment succeeded Stripe Test card number: 4242424242424242 04/24 242 42424
    -payment failed Stripe Test card number: 4000002500003155 04/24 242 42424

- Stripe webhook after deployment to Heroku
    * Stripe will only allow a single webhook endpoint associated with a synchronous webhook event.
    * Therefore have disabled the local host in Stripe to enable the webhook deployed by heroku app.

- Package HTML
    - Looks unfactored due to elif's, if /div's applied error would appear in code.
    * Works with or without closing divs but have removed due to potential of additional packages being applied.

- Checkout_Success HTML
    - Errors however design is due to package bing shown and elif's afe causing faults. Acceptable levels of errors as site works as required and if attempting to apply design becomes unsuitable.

## Credits and Acknowledgements

- Logos and case study images
    * Terry Downs - Accomplished graphic Designer who's interest is site for own work purposes.

- [Code Institute](https://codeinstitute.net/)
    * Tutor Support
    * Seun Owoni Koko for her guidance and support
    * Slack channel
        * Especially Emmett and Abi Harrison_alumni

- [Codepen](https://codepen.io/)
    * Excellent source to view and test HTML, CSS & JavaScript code

- [Stack overflow](https://stackoverflow.com/)
    * For the general queries that have happpened and the various solutions as guidance

- Website Designers
    * For their help in testing Mac version and advice on design

- Friends and Family
    * For their patience, advice and support

[Back to top ⇧](#introduction)

