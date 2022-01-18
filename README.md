<h1 align="center" id = "introduction">
     <a href="" target="_blank"><img src="" alt="Blank!"/></a>
     Project Kingsland
</h1>

<h2 align="center">
    <a href="" target="_blank">Kingsland Website</a>
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
    - [Consistency](#Consistency)
    - [Home](#Home-page)
    - [Login](#Login-page)
    - [Registration](#Registration-page)
    - [Profile](#Profile-page)
    - [Order Details](#Order-Details)
    - [Order Form](#Order-Form)
    - [Service and Contact](#Service-and-Contact-page)
    - [Browse](#Browse-page)
    - [Recipe view from browse page](#Recipe-view-from-browse-page)
    - [Recipe view from profile page](#Recipe-view-from-profile-page)
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
        - [GitHub deployment](#GitHub-deployment)
    - [Forking](#Forking-repository)
    - [Cloning](#Cloning-a-repository)
6. [Credits and Acknowledgements](#Credits-and-Acknowledgements)

***
![Responsiveness]()
***

## UX

### Aims

1. Clear understanding of site and business service with interactive features.

2. Easy navigation.

3. Responsive to all screens, sizes and browsers.

4. Comfortable understanding of data storage capability.

5. Safe and Secure payment function

6. Database management allowing for upload and download capability.

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
5. Be able to create a profile which is editable and deleteable.
6. Be able to view order history.
7. Be able to donload purchases from website.

#### Designer
This user is the site owner (or could be employed by the site owner to produce logo designs)
* The user wants to:
1. Receive notification of orders with purchase confirmation.
2. Have some detail on what is being requested to be designed.
3. Be able to upload designs onto database and assign to customer.
4. Be able to provide notification when service has been complete.
5. Be able to receive notification of contact queries directly from website.

#### Web Developer
This user is looking for imagery or influence for another project.

* They want to be able to:
1. Have easy navigation.
2. Find how the website was created.
3. Be able to see sources for design.
4. Be able to make contact with Developer/Site Owner.
5. Have an opportunity to clone site if wanting to use content.

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
    * Able to create, read, update and delete an order and their profile.
    * Make contact directly or through social sites.

2. Developer
    * Develop online presence through interactive actions on website.
    * Provide logo design ideas.
    * Receive notifications of orders.
    * Able to upload designs to website and store on secure database.
    * Confidently ensure logo designs are accessible by Developer and owner only.

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
    * Order creation, read, update and delete function
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
    * Contact Portal
    * Order creation, read, update and delete function
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
    * ![Council Culture]()

#### Imagery
1. Colours
    *   Contrasting bold colours to not take away imagery.
2. Imagery
    * Associations to:
        * Creativity
        * Business
        * Modern style with no curving corners of buttons or iamges

#### Page sections
1. Home
2. Login
3. Registration
4. Profile
5. Services
    * includes Contact form
6. Case Studies
7. Order form
8. Confirmation and payment form
9. Profile order details
    * To have download options
*  Potential pages to develop
    1. Other services
        - Stationary
        - Website design
        - Clothes printing


#### Structure

Hierarchical structure design for easy user navigation dependant on whether they are or are not registered:

![Site Structure]()

[Back to top ⇧](#introduction)



### Wireframe

- Designed in [Figma]()

- Desktop version
![Desktop wireframe]()

- Mobile version
![Mobile wireframe]()



[Back to top ⇧](#introduction)

## Features
This site has several pages for user to easily identify section associated. Navigation menu dependancy on user being or not being registered. Front end association to back end database and back end association to website for Designer/Developer.

### Django Framework
- pip (stands for pip install packages) can be used all kinds of tools within gitpod workspaces. This is used to install the Django framework into this workspace by typing "pip3 install django" into the Terminal. Note pip3 is installing Django for python version 3.
- To create a project "django-admin startproject kingsland_design ." was pushed from the terminal
    - This creates project in the current directory with files:
        * __init__.py - Directory to which files can be imported from
        * settings.py - Contains global setting for django project including which database to connect to
        * urls.py - Contains routing informatyion to type a specific url into address bar and will trigger python function
        * wsgi.py - Contains code to connect python with webserver application
- Migrations
    * code used to migrate "python3 manage.py migrate

- Superuser / admin creation
    * code to create an admin / superuser: "python3 manage.py createsuperuser" and then supplying a username, email address and a password
    * Admin access allows view of all django admin sites, emails, groups, orders, scoial accounts, etc .... in effect all apps imported from [django allauth documentation](https://django-allauth.readthedocs.io/en/latest/installation.html)

- Application Templates
    * These can be installed via Settings.py to bring in various templates created in Django.
    * This project uses user authenticaiton and model backend uploads for superusers.

- Django allauth
    * Install command: pip3 install django-allauth
    * provides apps for allowing user logins either directly or via social media sites for this project. It can also allow for easier payment, e.g. apple or google pay to make user experience smoother. ---- check this has been done in time for project submission, otherwise caveat this has been installed but not utilised for this project -----

- Email authentication
    Allauth account allows for email verification but as created using superuser the verification has to be done via admin account in django.

### [Database](AWS)
- AWS used to store data under database name ""
    * Collections to store specific data:
        * 


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

*![Kingsland Palette]()

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
        * Service
        * Contact
        * Order form
    - Leading member to
        * Case Studies
        * Service
        * Contact
        * Profile
        * Order form
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
    - Full name
    - Email (to be used as unique username)
    - Password

3. Register button if details correct.
    - Data is passed through to AWS

4. Warning if detail format incorrect.

5. If already registered, warning to state so and to direct user to Login page.


### Profile page
1. For members logged in only, non members will not be able to view.

2. Welcome flash message.

3. Profile details - associated to database.
    - Edit account function
        * This to include ability to update password
    - Delete account function

4. Orders - associated to database.
    - Historic orders
        * Summary of orders
    - Ability to create a new order

### Order Details
1. For members logged in only, non members will not be able to view.

2. Welcome flash message.

3. Orders - associated to database.
    - Historic orders
        * shows detailed requests
        * If completed images of logos
        * Download options
    - Ability to create a new order


### Order Form
1. Data obtained from form updates.

2. Package selections made here.

3. Submit button
    * If registered, directs to confirmation and payment page.
    * If not registered, directs to registration page.

[Back to top ⇧](#introduction)
    
### Service and Contact page
1. Hero-image

2. Steps on how to use service

3. Contact section
    - Full name
    - Email
    - Subject
    - Message
    - Submit button

2. Associated to EmailJS ---- ? ------

3. Email to Developer/Designer and Customer Auto Reply with appropriate message and link to site.


### Case Studies page
1. Leads from images selected in Home Page

2. Images of logo associations to company

3. Description of how each were designed

4. Option to create order


### Payment page
1. Hero image
    - highlighting safety and secure purchase

2. Confirmation of order details being submitted.
    - Edit button option if incorrect leading user back to order creation section

3. Confirmation of order package being purchased
    - Option to select another package if incorrect

4. Form to obtain payment details
    - Submit button to lead to Stripe payment process

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

- [AWS-Amazon Web Service)](https://aws.amazon.com/)

- [Heroku](https://www.heroku.com)

- [Coolors - colour collage](https://coolors.co)

- [Picjumbo](https://picjumbo.com)

- [Unsplash](https://unsplash.com/)

- [Github](https://github.com)

- [Gitpod](https://www.gitpod.io)

- [Bootstrap v4.4](https://getbootstrap.com)

- [MDBootstrap version 4](https://mdbootstrap.com)

- [Google fonts](https://fonts.google.com)

- [Figma]()
    * [project wireframe]

- [Random Key Generator](https://randomkeygen.com)

- [Font Awesome](https://fontawesome.com)

- [Bootstrapcdn](https://www.bootstrapcdn.com)

- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x)

- [cdnjs](https://cdnjs.com)

- [EmailJS](https://www.emailjs.com)

- [Codepen](https://codepen.io)

- [Am I responsive](http://ami.responsivedesign.is)

- [HTML code checker](https://validator.w3.org)

- [CSS code checker](https://jigsaw.w3.org/css-validator)

- [JS Hint JavaScript validator](https://jshint.com/)

- [PEP8](http://pep8online.com/)

- [Gif Compessor](https://www.freeconvert.com/gif-compressor)

- [Browser site testing - BrowserStack](http://browserstack.com)

- [RGBlind chrome extension]

- [Eye Dropper extension]

[Back to top ⇧](#introduction)


## Testing 
-   ### View [TEST.md file](https://github.com/TezBaydu/Milestone-project-4-GraphicDesign/blob/main/TEST.md)

### Commits

- Over --?-- commits

### Code Testing
- HTML 
- CSS
- JavaScript
- JQuery
- Python

### Element testing
- Ensure elements behave as expected
   
### Device testing

- [Am I responsive](http://ami.responsivedesign.is)

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
    * ![git-commits]()

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
    4. Automatic deployment can be done via the GitHub repository where this project is stored.
    5. Select connect to GitHub button and when pressed make sure your GitHub profile is displayed and then add your repository name in "repo-name" field and click search.
    6. Once the repository is found, click "Connect" to connect to this app.
    7. For thie project DO NOT PRESS "ENABLE AUTOMATIC DEPLOYS" YET !!
        - This is because there are sections in files not deployed to GITHUB that need to be manually enabled first.
    8. Select "Settings".
    9. Select "Reveal Config Vars".
    10. Sections within env.py file are added to this section.
    11. WARNING: Ensure requirements.txt & Procfile are added to repository prior to Heroku deployment or Heroku will not see these when connecting.
    12. Within Heroku you should now be able to safely press the "Enable Automatic Deploys" button. Select Deploy section to view.
    13. Select "ENABLE AUTOMATIC DEPLOYS".
    14. Select "Deploy Branch" after selecting which version you wish to deploy. Then Wait for Heroku to load all files.
    15. Once done you should see "Your app was successfully deployed" and a "View" button.
    16. Select "View" button to launch the app.
    17. As this is connected to GitHub, Heroku will obtain changes when these are pushed to the GitHub repository.

#### DEBUG
- Ensure within app.py change "debug=True" to "debug=False"

### GitHub deployment
- Not attempted for this site but referenced here in case required in future

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

## Credits and Acknowledgements

- [Code Institute](https://codeinstitute.net/)
    * Tutor Support have been amazing !!
    * Seun Owoni Koko for her enthusiasm, guidance and support
    * Slack channel

- [Codepen](https://codepen.io/)
    * Excellent source to view and test code

- [Stack overflow](https://stackoverflow.com/)
    * For the general queries that have happpened and the various solutions as guidance

- Website Designers
    * For their help in testing Mac version and advice on design

- Friends and Family
    * For their patience, advice and support

[Back to top ⇧](#introduction)

# Re-Plan:
    - Choose Package (choice of 3)
    - pushes to package detail
        * This could contain a form for details
        * On submit it pushes to a bag area
        * This allows for several selections if required
            - for any interim sales companies who may have several clients they may represent
    - Package detail to have push to checkout
        * checkout to have payment details and personal details

# Session detail delete
    - To delete data as part of testing this can be done by selecting:
        * right click screen
        * click inspect
        * select Application
        * select Cookies
        * Right click session ID
        * select delete
    - To delete storagte from site datae
        * right click screen
        * click inspect
        * select Application
        * select Storage
        * right hand pane select 'Clear site data'

# Django responsive design
    - django-responsive2 0.1.3 installed for responsive s=designs using django
        * pip3 install django-responsive2
[django-responsive2](https://django-responsive2.readthedocs.io/en/latest/readme.html#)
        * Applied and adjusted into settings but responsive adjustment not working
        * worth a try....!

# Stripe
[TempMail](https://temp-mail.org/ ) 
- Email : gekil23029@tinydef.com
- Full Name: ge kil
- Country: United Kingdom
- password: c0d%5Tr16E

* Stripe is a digital platform to allow for payments on eCommerce stores
    * JS code is applied to base.html to allow for Stripes fraud detection features
    * API Keys STRIPE_PUBLIC_KEY  and STRIPE_SECRET_KEY - are required and are applied in Gitpod workspace variables

* Remember pip3 install stripe when coming back into project

# Requirements file
- To Freeze into file: pip3 freeze > requirements.txt

# Bugs & Issues
- base.css: not working - project-header in project.html not giving a margin-top - associated to Base.html not in allauth
    - Has been applied

- JSON migrations: Best to plan what is to be migrated in advance. This to save the deletion of JSON files and migrations and starting over as I had not updated descriptions for companies:
    * Done by
        1. Delete all files from Companies and Projects in Admin
        2. Delete db.sqlite3 file in DATABASE.md
        3. Delete all files in migrations folder except __init__.py
        4. Ensure you update JSON files, views.py, models.py and amdin.py prior to actions below
        5. python3 manage.py makemigrations --dry-run: This is useful to see if there are any requirements i.e. install pillow for images.
        if ok
        6. python3 manage.py makemigrations
        if ok
        7. python3 manage.py migrate --plan: This is useful to see and make sure you are only migrating app in particular, otherwise state the file after to ensure this is the only one captured.
        if ok
        8. python3 manage.oy migrate (name of file if applicable)
        9. python3 manage.py loaddata companies.json and then projects.json
    * superuser will also be deleted so you will need to re-create the superuser
        1. python3 manage.py createsuperuser

- To create through Django
    * in terminal type: python3 manage.py startapp (name of folder)
    * add into settings.py of main project name

- Structure workflow not quite working as expected and advised through Tutorship to utilise Packages as Orders and they can be placed into a bag under order detail.
    * Having to remove code and re-work migrations in this format

- css not showing images
    * When this occurs, ensure cache is cleared as a pimary check: windows ctrl-f5

- extra css not locating
    * python manage.py findstatic --verbosity 2 packages.css: code to see if is looking in appropriate directory
    issue with packages extra css not being found. To update base.css to ensure this doesn't delay project any further.
        - Have since found base.html not in allauth and have updated.
            * Issue to note - when updating css in static folders these may not at first appear. Requires either a clear cache command (CTRL+F5) or stop server and re-run it.

- Package description
    * A text was too long for styling and although passed over via JSON this has been amended in Admin
        * quality-request change from "Downloadable" High Quality content to "Download" High Quality content

- Object set not serializable
    * packages list created but as there was more than one object to pull a list had to be created. This had to sit in [] to be serializable not {} !!
    * even so this wasn't actually needed and was removed altogether and the call made in contexts.py
    * This caused further issues as now no detail was being called and being pulled into bag. Previous calls were stored in session and this was being called instead.
    * Once cleared it was identificed there was a requirement to update add_to_bag and contexts.py, however another issue arrived where you could only add one of each package at a time. This would confuse user and so site re-design so only 1 package and purchse can be created, edited, deleted at a time. But one purchased it is stored as unique.

- Messages not appearing when pushing items into bag...?! have been thorugh and updated Package, bag-item association not working in views.py
    * Resolved after updated to Package and clearing site data and re-applying

- Adjust Bag
    - Advised to use local storage session for package details
            - New template created for edit but failed help requested from tutor Support
            - Advised to set up CompanyDetails in packages models in order to identify companyu details intialised and if adjusted these can be compared to for update
            - Subsequently advised other approach to iterate over bag local storage session could have worked
            - Code has become very complex for bag view and feels like a week and a half of work has been wasted
    - Highlighting an already edited bag can be re-edited and this adds to the Company Details admin. This is not a major issue as the function to edit is workable and potential this can be looked into but have spent over 1 and a half weeks just on this...potential coding to improve.

- CompanyDetails
    - Sku not appearing in Admin?
        * Attempted adding uuid logo_request_number but not appearing - Done - applied def save function in packages models

    - Initiate pacakge app in line for use similar to bag - Done
    - Remove package - Done - Improvements to have an extra warning to remove but not covered

- Bag session store
    - Even when applying a model for CompanyDetails (The details associated to each logo request) the details do not store in bag when the user signs out.
        * Potential improvement to make to site in future

- Getting lots of errors which may stem from settings
    * had run pip3 freeze > requirements.txt and this has pulled a much larger list from somewhere....? but hve no idea....could be because of the amount of times this file hs been shared.

- django install
    When installing django, ensure it is done using command pips install django==3.2.9, django 3.4 version isn't applicable to **KWARGS. Boutique Ado project states django version used is 3.3.

- django install after initial access
    * Slack solution : Run 'pip3 install -r requirements.txt' in terminal

[Deleting migrations](https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html)

- checkout_success error
    - TypeError at /checkout/
Field 'id' expected a number but got ('1', {'company_name': 'Checkout success Test5', 'company_slogan': 'Checkout success Test5', 'company_description': 'Checkout success Test5', 'company_colors': 'Checkout success Test5', 'company_look': 'Checkout success Test5', 'logo_request_number': '8D715DB6E62E436596DF4C963C372C82'}).
    - /workspace/Milestone-project-4-GraphicDesign/checkout/views.py, line 36, in checkout
                    package = Package.objects.get(id=item_id) 
    - contexts.py appends logo detail (CompanyDetail) onto bag_items and when called into OrderLineItem in Checkout as company_details it looks like it is appending this detail to the field id causing an error....Potential aim to use Logo Request Number in CompanyDetails or is this barking up the wrong tree....?

- settings.py Django SECRET_KEY
    - Ensure Secret key is placed into gitpod environment to call prior to submission

- Site Overhaul
    - When attempting to checkout the following error occurs due to the field id being treated as a list: TypeError: Field 'id' expected a number but got {'company_name': 'Company change', 'company_slogan': 'Company change', 'company_description': 'Company change', 'company_colors': 'Company change', 'company_look': 'Company change', 'logo_request_number': 'AE5594F2C61345EB937B926DBB079AA9'}
    - After several Tutor discussions and student discussion the conclusion is due to wanting to update CompanyDetails in the bag and then pulling this thorugh into checkout. As the company_details are in the bag so is updatable it appends it onto the field 'id' and therefore as it is looking for a number it is not identifiable to pull through to checkout_success. However Stripe is accepting the data as is the Admin...it just doesn't push through to the checkout_success page.
    - Due to time constraints I am forced to overlook having a form which is updateable separate to Package and going to revert to omitting CompanyDetails model. This is at commit 88 as a start as I think this is a feature I'd like to resolve in the future.

- Stripe Webhook
    - Have applied code for Stripe Webhook and issue with key recognition.
    - These are a variable call in gitpod instance where the Public and Secret Key are accepted but the webhook key is showing a 401 error. After investigation this is stated to be a key call issue however these have been coped and applied several times and still having an issue with error.
    - This is something to address if time allows prior to project submission but have been notified this is 't a huge requirement for the project but is certainly something to have for an actionable purchase in a site.

- Stripe Error 404
    - Resolved by making PORT 8000 Public

- Stripe Error 500
    - Resolved as was a typo (usual cause for Error 500) STRIPE_WH_SECRET instead of STRIPE_WH_KEY

# To Do

[Temp email site](https://temp-mail.org/en/)
        * Temp mail used: renenag259@latovic.com
        * Temp password
    - Services app
        * Contact details and form - Almost Done
    - Deploy to heroku
    - Email notifications
        * To customer - Done
        * To Admin for order update and action
    - Admin upload images to Django admin and onto user profile - ? POtential to leave but nice to have

# Mentor questions
- Contact form not pulling authenticated users
- Contact form not pulling detailapplied into fields
- Package disappears from orders when deleted or adjusts Totals
    - Only association is with the pid number in Stripe to find the amount charged however pacakge details with logo request details disppaears?
- django install required
- advice on user profile where images are to be loaded into django admin and this pulls into user profile - Don't think have enough time
- webhook error - Off and On








        











