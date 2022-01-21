<h1 align ="center" id = "top">Kingsland Test file
<h1>

<h2 align="center">
    <a href="https://kingsland-design.herokuapp.com/" target="_blank">Kingsland Website</a>
</h2>

<h3 align="center">
    <a href="https://github.com/TezBaydu/Milestone-Project-4-GraphicDesign#README" target="_blank">Back to README file</a>
</h3>

## Contents
1. [Commits](#Commits)
2. [User Story testing](#User-Story-testing)
    - [Browsers](#Browsers)
    -[Customers](#Customers)
    -[Designer](#Designer)
    - [Web Developer](#Web-Developer)
3. [Code testing](#Code-testing)
    - [HTML5](#HTML5)
    - [CSS3](#CSS3)
    - [JavaScript](#JavaScript)
    -[PEP8](#Python-PEP8)
4. [Element testing](#Element-testing)
    - [Navigation bar](#Navigation-bar)
    - [Scroll Top button](#Scroll-Top-button)
    - [Footer](#Footer)
    - [Page Tests](#Page-tests)
        * [Home](#Home)
        * [Register](#Register)
        * [Login](#Login)
        * [Case Studies](#Case-Studies)
        * [Packages and Detail](#Packages-and-Package-Detail)
        * [Bag](#Bag)
        * [Checkout and Detail](#Checkout-and-Order-Detail)
        * [Checkout Email](#Checkout-email-confirmations)
        * [Stripe Checkout](#Checkout-payment-succeeded-in-Stripe)
        * [Profile](#Profile)
        * [Package Admin](#Package-Admin)
        * [Contact](#Contact-Page)
        * [Contact Emails](#Contact-emails)
5. [Device testing](#Device-testing)
6. [Colour blindness testing](#Colour-blindness-testing)
    - [Protanopia](#Protanopia)
    - [Deuteranopia](#Deuteranopia)
7. [Browser testing](#Browser-testing)
8. [User testing](#User-testing)

## Commits
- Over 175 commits
- Commits made in as many instances as possible however there have been instances where code had to be revised but when passed certain stages of development it was thought best to carry the commits instead of branching.

[Back to top ⇧](#top)

## User Story testing

### Browsers
The user is wanting to design ideas for logos

* This user wants to:
1. Be able to navigate through the website easily.
    - Responsive collapsible fixed nav menu for user to see more of screen and be able to navigate when required.
    - Various links to other pages.
2. View designs of other projects.
    - Logos linked to relevant case study at home page.
    - Designs used in various formats.
    - Easy filter options for each case study.
3. Be able to navigate to relevant social links.
    - Always an option to select from fixed footer.
4. Be able to make contact for queries and newsletter sign up.
    - Easy to gain contact via navbar from link in footer.
    - Immediate contact made through auto notification.
    - Email notification sent to user contact has been made.

### Customers
The user is wanting to make a purchase to obtain a business logo
*   This user wants to:
1. Be able to navigate through the website easily.
    - Responsive collapsible fixed nav menu for user to see more of screen and be able to navigate when required.
    - Various links to other pages.
    - Able to login from nav bar.
    - Local data can store login details even though password is not passed through to database.
2. Easily view designs and case studies of design impact.
    - Logos linked to relevant case study at home page.
    - Easy filter options for each case study.
3. Be able to navigate to relevant social links.
    - Always an option to select from fixed footer.
4. Be able to create a profile which is editable.
    - Profile is created upon registration.
    - Profile will hold editable details.
    - Username and email is non editable to ensure orders are associated to origin user source
5. Ability to make a purchase
    - Bag store and checkout function on registration.
    - Secure payment system utilising Stripe facility.
    - Warnings showing failure if values are incorrect.
6. Be able to view order history.
    - Profile holds order history.
    - Shows summary but has link to order detail and reference number.
7. Be able to make contact for queries and newsletter sign up.
    - Easy to gain contact via navbar from link in footer.
    - Immediate contact made through auto notification.
    - Email notification sent to user contact has been made.
    - Username and email updated if registered.

### Designer
This user is the site owner (or could be employed by the site owner to produce logo designs)

* The user wants to:
1. Receive notification of orders with purchase confirmation.
    - Once purchases are made, details are stored in admin and email notification sent to Designer.
2. Have some detail on what is being requested to be designed.
    - Some detail on emails but to view Admin for full instruction.
3. Be able to receive notification of contact queries directly from website.
    - Email notification received when queries are made showing customer message.
4. Be able to identify orders from a user to action.
    - Email notification shows reference to order where full details can be obtained from Admin.

### Web Developer
This user is looking for imagery or influence for another project.

* They want to be able to:
1. Have easy navigation.
    - Responsive collapsible fixed nav menu for user to see more of screen and be able to navigate when required.
    - Various links to other pages.
2. Be able to make contact with Developer/Site Owner.
    - Able to make contact through contact / enquiry page of site.
3. Have an opportunity to clone or fork site if wanting to use content.
    - Readme can be shared which has secure details of ability to clone or fork repository
4. Option to access repository if authorised
    1. Find how the website was created.
        - [README.md](https://github.com/TezBaydu/Milestone-Project-4-GraphicDesign#introduction) file created detailing why and how website was created.
        - Contact form can also be used for General enquiries.
    2. Be able to make contact with Developer.
        - Contact form can be used for general enquiries.
        - [README.md Deployment](https://github.com/TezBaydu/Milestone-Project-4-GraphicDesign#Deployment) has description of cloning and forking and therefore contact can be made via GitHub.
    3. Have an opportunity to clone site if wanting to use content.
        - [README.md Cloning](https://github.com/TezBaydu/Milestone-Project-4-GraphicDesign#Cloning-a-repository) has description of cloning.

[Back to top ⇧](#top)

## Code Testing

### HTML5
- [HTML code checker](https://validator.w3.org/)
     
    - Tests during development, record stored below
    - Test date 21/01/2022
        - HTML5 test
            * Home
                - ![HTML5 test](media/html-home.JPG)
            * Case Studies
                - ![HTML5 test](media/html-projects.JPG)
            * Packages
                - ![HTML5 test](media/html-packages.JPG)
            * Packages Detail
                - ![HTML5 test](media/html-packages-detail.JPG)
            * Add Package
                - ![HTML5 test](media/html-packages-add.JPG)
            * Edit Package
                - ![HTML5 test](media/html-packages-edit.JPG)          
            * Bag
                - ![HTML5 test](media/html-bag.JPG)
            * Checkout
                - ![HTML5 test](media/html-checkout.JPG)
            * Checkout Success
                - ![HTML5 test](media/html-checkout-success.JPG)
                    * Errors due to django if statements to call associated package.
                    * Acceptable as functional in front end.
            * Contact 
                - ![HTML5 test](media/html-contact.JPG)
            * Profile
                - ![HTML5 test](media/html-profile.JPG)
            * Login
                - ![HTML5 test](media/html-login.JPG)
            * Register
                - ![HTML5 test](media/html-register.JPG)   

### CSS3
- [CSS code checker](https://jigsaw.w3.org/css-validator/)
- Tests during development, record stored below
    - Test date 21/01/2022
        - CSS test
            * Home
                - ![CSS test](media/css-home.JPG)
            * Case Studies
                - ![CSS test](media/css-projects.JPG)
            * Packages
                - ![CSS test](media/css-packages.JPG)
            * Packages Detail
                - ![CSS test](media/css-packages-detail.JPG)
            * Add Package
                - ![CSS test](media/css-packages-add.JPG)
            * Edit Package
                - ![CSS test](media/css-packages-edit.JPG)          
            * Bag
                - ![CSS test](media/css-bag.JPG)
            * Checkout
                - ![CSS test](media/css-checkout.JPG)
            * Checkout Success
                - ![CSS test](media/css-checkout-success.JPG)
            * Contact 
                - ![CSS test](media/css-contact.JPG)
            * Profile
                - ![CSS test](media/css-profile.JPG)
            * Login
                - ![CSS test](media/css-login.JPG)
            * Register
                - ![CSS test](media/css-register.JPG)  


                
### JavaScript
- [JS Hint JavaScript validator](https://jshint.com/)

    - Test date 21/01/2022
        * All Template scripts
            ![JSHint warnings](media/js-html.JPG)
        * Checkout
            ![JSHint warnings](media/js-checkout.JPG)
                -   Stripe variable unused, advised to use stripe, however this is taken from a call two lines above under #ID so is usable.
        * Profiles
            ![JSHint warnings](media/js-profiles.JPG)
                - 



### PEP8
- Used Django code python3 -m flake8

    - Test date 21/01/2022
        * Code issues
        ![PEP8 Test](media/flake8-checkout.JPG)
            * import error in checkouts app.py
                * Acceptable linting issue as importing invokes code, however linter doesn't know and so produces an error.

[Back to top ⇧](#top)

## Element testing
### Navigation bar
- Test 
    * Responsive hover on click.
    * Links.
![Navbar test](media/navbar.gif)

### Scroll Top button
- Test 
    * Button appears on scroll down and when pressed scrolls user to top
![Scroll Top button test](media/scroll-button.gif)

### Footer
- Test 
    * Social links change on hover
    * Social links lead to associated sites
![Footer social links test](media/footer-links.gif)

[Back to top ⇧](#top)

### Page tests
#### Home
- Image
    * Nav links to other pages
    ![Home Page test](media/home.gif)

[Back to top ⇧](#top)

#### Register
- Image
    * Appealing
- Inputs
    * Email validation
    * Password hidden
    * Link to login if already registered
    * Message success popup
    ![Register Page test](media/register.gif)


#### Login
- Image
    * Appealing
- Inputs
    * Email
    * Password hidden
    * Warning if incorrect
    * Link to Register if not a member
    * Message success popup
    ![Login Page test](media/login.gif)

[Back to top ⇧](#top)

#### Case Studies
- Images
    * Appealing
- Projects
    * Buttons to link to different porjects
    * Description at bottom
    * Link to Packages
    ![Case Studies test](media/projects.gif)

#### Packages and Package Detail
- Packages available images and text
    * Packages separated
    * admin view to have edit or deactivate/activate button
        - This so it can be viewed or not by public
    * Ability to select in isolation and consider prior to adding to Bag
    ![Packages test](media/packages.gif)

[Back to top ⇧](#top)

#### Bag
- Package added from Package Detail
    * Popup showing bag updated
    * Bag showing chosen Package
    * Unable to choose another package as one is already selected
        - Popup message stating error and reason
    * Ability to remove and apply a different Package
    ![Bag test](media/bag.gif)

#### Checkout and Order Detail
- Chosen Package
- Logo request details
- Billing and contact details
    * Option to save details to profile
- Payment method
    * Error if fails
    * Success to show popup message and order details
    ![Checkout test](media/checkout.gif)

#### Checkout email confirmations
- Email to customer confirming order
- Email to Admin confirming order has been made
![Checkout email test](media/checkout-emails.gif)

#### Checkout payment succeeded in Stripe
![Stripe payment success](media/stripe-payment-succeeded.JPG)

#### Order in Admin
![Order in Admin](media/admin-order.JPG)

#### Profile
- Profile details
    * username
    * Email
    * ability to update name, number and address
- Order Summary details
    * Order number linked to Order details
    ![Profile Page test](media/profile.gif)

[Back to top ⇧](#top)

#### Package Admin
For use by Admin if new packages or services become available
- Add Package
    * Name
    * Sku
    * Friendly Name
    * Logo Count request
    * Quality Request
    * Support request
    * Production Days
    * Price
    * Select Image
    * Option to make active
        - Potential admin may want to view prior to public view activation
    * Cancel button
    * Add Package Button
    * Lead on to view Package applied
    ![Add Package test](media/package-add.gif)
- Edit Package
    Ability to edit fields and add an image
    ![Edit Package test](media/package-edit.gif)
    ![Edited Package in group test](media/package-edit-ingroup.gif)

[Back to top ⇧](#top)

#### Contact Page
- Information of steps on how to order
    * Appealing and clear images
- Contact form
    * Contact fields are editable
    * All fields are required
    * Email field requires email format
    * Submit button works
    * Pop up appears to show success
    * Contact fields updated with user detail if registered
    * Position returns to Home after submission
    - ![Contact Page test](media/contact.gif)

#### Contact emails
- Email to customer confirming enquiry has been made
- Email to Designer / Admin confirming an enquiry has been made with subject and a contact email
    - ![Customer and Admin Contact Email test](media/contact-emails.gif)

[Back to top ⇧](#top)

### Device testing
- [multi-mockup](https://techsini.com/multi-mockup/index.php)
    * Device styles and responsiveness for Mobile, Tablet and Desktop
    ![Device responsive test](media/device-responsive.gif)

[Back to top ⇧](#top)

### Colour blindness testing

#### Protanopia
- ![Protanopia test](media/protanopia.gif)

#### Deuteranopia
- ![Deuteranopia test](media/deuteranopia.gif)

[Back to top ⇧](#top)

### Browser testing
- Microsoft Edge browser testing
    * ![Microsoft Edge browser test](media/microsoft-edge.gif)

- Firefox browser testing
    * ![Firefox browser test](media/firefox.gif)

- Safari browser testing
    * Unable to test without making a purchase
    * Have been advised by Friends who own Macs design and interactivity was fine
    * Images below
        - Safari
    * ![Safari browser test](media/safari.jpeg)
        - Safari new silicone Mac
    * ![Safari new Silicone Mac browser test](media/safari-new-silicone-mac.jpeg)

[Back to top ⇧](#top)

### User testing
- Friends
- Family
- Website Designers

[Back to top ⇧](#top)

<h2 align="center">
    <a href="https://kingsland-design.herokuapp.com/" target="_blank">Kingsland Website</a>
</h2>

<h3 align="center">
    <a href="https://github.com/TezBaydu/Milestone-Project-4-GraphicDesign#README" target="_blank">Back to README file</a>
</h3>
