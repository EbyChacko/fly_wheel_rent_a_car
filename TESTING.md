# Flywheel rent a car
# Testing

Below is the testing performed for the project. Wherever possible, screenshots were taken to document the testing.


## Lighthouse

The site was tested using Lighthouse in Chrome DevTools to check performance, accessibiltiy, best practices and SEO. Where possible, errors and warnings were corrected so all final results were a minimum of 90. The final testing on Lighthouse was run on incognito mode. The results are below.

<details>
<summary>Lighthouse Home</summary>

![Index](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717536668/Royal%20Drive/readme/home_scdyvk.png)
</details>

<details>
<summary>Lighthouse About us</summary>

![About us](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717536669/Royal%20Drive/readme/about_us_duvz0q.png)
</details>

<details>
<summary>Lighthouse Contact Us</summary>

![Contact Us](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717536852/Royal%20Drive/readme/contact_tlvpjs.png)
</details>

<details>
<summary>Lighthouse search cars</summary>

![search cars](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717536853/Royal%20Drive/readme/Search_car_aumlpl.png)
</details>

<details>
<summary>Lighthouse Search result</summary>

![Search result](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717537224/Royal%20Drive/readme/search_result_gfv3he.png)
</details>

<details>
<summary>Lighthouse car details</summary>

![car details](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717537225/Royal%20Drive/readme/Car_details_gwgqun.png)
</details>

<details>
<summary>Lighthouse Checkout</summary>

![Checkout](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717537480/Royal%20Drive/readme/checkout_page_as5qh2.png)
</details>

<details>
<summary>Lighthouse Profile</summary>

![Profile](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717537551/Royal%20Drive/readme/profile_zgyg7p.png)
</details>

<details>
<summary>Lighthouse Booking Details</summary>

![Booking Details](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717537664/Royal%20Drive/readme/booking_details_ddo1v5.png)
</details>

<details>
<summary>Lighthouse Terms and conditions</summary>

![Terms and conditions](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717538715/Royal%20Drive/readme/terms_and_conditions_dhjvxe.png)
</details>

<details>
<summary>Lighthouse update profile form</summary>

![update profile form](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717538820/Royal%20Drive/readme/update_profile_form_aowxf2.png)
</details>

<details>
<summary>Lighthouse privacy policy</summary>

![ privacy policy](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717539030/Royal%20Drive/readme/privacy_and_policy_pkamnp.png)
</details>

## HTML Validator

HTML was tested through validation by copying the source code of pages into the direct input on [W3C HTML Validator](https://validator.w3.org/#validate_by_input).
Any errors found where then corrected to meet the validator's standards. Below are the results after templates were edited to meet the requirements.

<details>
<summary>Index</summary>

![Index](readme-docs/testing/validate_index.webp)
</details>

<details>
<summary>FAQ</summary>

![FAQ](readme-docs/testing/validate_faq.webp)
</details>

<details>
<summary>Privacy Policy</summary>

![Privacy Policy](readme-docs/testing/validate_privacy.webp)
</details>

<details>
<summary>Latest Products</summary>

![Latest Products](readme-docs/testing/validate_latest.webp)
</details>

<details>
<summary>Category</summary>

![Category](readme-docs/testing/validate_category.webp)
</details>

<details>
<summary>Product</summary>

![Product](readme-docs/testing/validate_product.webp)
</details>

<details>
<summary>Profile</summary>

![Profile](readme-docs/testing/validate_profile.webp)
</details>

<details>
<summary>Profile Reviews</summary>

![Profile Reviews](readme-docs/testing/validate_profile_reviews.webp)
</details>

<details>
<summary>Profile Recipes</summary>

![Profile Recipes](readme-docs/testing/validate_profile_recipe.webp)
</details>

<details>
<summary>Management Dashboard</summary>

![Management Dashboard](readme-docs/testing/validate_mgmt_products.webp)
</details>

<details>
<summary>Management Reviews</summary>

![Management Reviews](readme-docs/testing/validate_mgmt_reviews.webp)
</details>

<details>
<summary>Management Recipes</summary>

![Management Recipes](readme-docs/testing/validate_mgmt_recipes.webp)
</details>

<details>
<summary>Management Comments</summary>

![Management Comments](readme-docs/testing/validate_mgmt_comments.webp)
</details>

<details>
<summary>Management Submitted Recipes</summary>

![Submitted Recipes](readme-docs/testing/validate_mgmt_submitted.webp)
</details>


## CSS Validator

No errors were found in the CSS was manually copied into the [W3C CSS Validatory](https://jigsaw.w3.org/css-validator/)

<details>
<summary>Base CSS</summary>

![CSS Validation](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717554786/Royal%20Drive/readme/CSS_validation_base_touunj.png)
</details>

<details>
<summary>Checkout CSS</summary>

![Checkout CSS Validation](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717554961/Royal%20Drive/readme/CSS_validation_checkout_izizat.png)
</details>


<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
            alt="Valid CSS!" />
    </a>
</p>


## JavaScript Testing

JavaScript validation was performed using [JSHint](https://jshint.com/) to check quality of the JS scripts. 

<details>
<summary>JSHint Checkout and Stripe</summary>

![Stripe](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717555337/Royal%20Drive/readme/JS_validation_Checkout_fdzbd6.png)
</details>


## Python Testing


[CI Python Linter](https://pep8ci.herokuapp.com/) was used to check all the pages to confirm there were no linting issues. the following was the results for all the '.py' files

<details>
<summary>Python PEP8 test result</summary>

![Python PEP8 test result](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717557363/Royal%20Drive/readme/PEP8_Home_signals_t3wmzz.png)
</details>


## Manual Testing
Below the steps for manual testing of the site have been arranged into tables. All available incidents on the website have been manually tested, and the results are as follows: <br>
### **Before sign Up / Login**
| **Feature** | **Action** | **Expected Result** | **Actual Result** | 
|-------------|------------|---------------------|-------------------|
| Open the website | Click the link | Open the home page | Works as expected |
| SignUp & login Buttons | When open the website before login | Must show the sugnup/ login button | Works as expected |
| Flywheel rent a car details visible to all the visiters | open the website | User can navigate though all the details of the flywheel rent a car including Home,About us and contact us pages | Works as expected |
| signup or login page | click on ony of the rent a car button | as the rent a car option is restricted to only the user who are authenticated. So redirected to to a a page signup or login | Works as expected |
| Footer Links | click on the links | Navigate to deferent pages same as the header Nav buttons | Works as expected |
| Click the number/ email to open call/email option | click the number/email | clicking on the number/mail will open the call/ mail app | Works as expected |
| Social Media | click on the icon in the footer | Open the social media app | Works as expected |
|contact us page | click on the contact us button | A contact page is open with necessory contact details, additionally a form is avilable to write any message to the hospital if the user want to| Works as expected |
| contact form | input invalid data and submit | error messages shown | works as expected |
| contact form | input valid data and submit | message submitted and show a confirmation message | works as expected |
| Booking Creation only for authorised users | click on any of the "rent a car" button in the website before login | Navigate to the Signup / login Page to inform the user that to create an appointment, they should signup or login | Works as expected |
| Fade-in animation works | on loading page | A fade-in animation is expected to happen for the home page when the user open the website | Works as expected|
| logo animation carausel | page load | an automated animation carausel of deferent car company logoes | Works as expected |
|Subscribe form | input mail id and click subscribe button | The given mail id is save in the mail chimp account for future use | Works as expected |

### **Sign Up**
| **Feature** | **Action** | **Expected Result** | **Actual Result** | 
|-------------|------------|---------------------|-------------------|
| signup page | Click the signup button | Open the signup page | Works as expected |
| form submission fails | input invalid details | Show error in the form | Works as expected |
|form submission success | input valid details | navigate to the success page display a message "confirmation mail has been send to the email" and send an email with the link to confirm the email | works as expected |
| Confirm the email page | Click on the link provided in the email | navigate to the website page with a button "confirm" | Works as expected |
|confirm email | Click on the "Confirm" button | The email will be confirmed and navigate to the login page with a success message | Works as expected |

### **Login**
| **Feature** | **Action** | **Expected Result** | **Actual Result** | 
|-------------|------------|---------------------|-------------------|
| Login page |  Signup/Click the signup button in the navbar | Open the login page | Works as expected |
| login form fails | Input invalid details | Show error in the form | Works as expected |
|login for success | Input valid data(username and password) | Navigated to homepage with success message and the signup and login button disappear, also the user name and logout buttons visible in the navbar | Works as expected |

### **After Login**
| **Feature** | **Action** | **Expected Result** | **Actual Result** | 
|-------------|------------|---------------------|-------------------|
|home, about us,and contact pages | click on each button | Works as same as before login | Wors as expected |
| Search car | click on ony of the 'rent a car' button | if the user is authenticated, it will navigate to the car search page | works as expected |
| User name button | click on the user name in the navbar | a drop down menu will appear with "my prifile" and "Update Profile" buttons | Works as expected |

### **Car search and Booking**
| **Feature** | **Action** | **Expected Result** | **Actual Result** | 
|-------------|------------|---------------------|-------------------|
|car search form | click on ony of the 'rent a car' button | if the user is authenticated, it will navigate to the car search page with a search form | works as expected |
| car search form fail | input invalid data like pickup date is after drop off date | show form error | Works as expected |
|Car search success | Input valid data | load the search result page with available car and its details | works as expected |
|car search without any car | search the car with valida data | if any of the car in the flywheel is not available on the input date, at the pickup location, an empty result page with a message to search for other location or date. | Works as expected |
| Filter form | click on the filter button in the search result page | A filter form will appear in the same page with additional filters like gearbox, number of searts etc. | works as expected |

## Browser Compatibility

The website was tested on:

- Chrome Version 108.0.5359.125
- Firefox Version 108.0
- Edge Version 108.0.1462.54
- Safari iOS Version 16.1.1


## Bugs
### Fixed Bugs

- Comment options:
    - **Issue**: "Edit" and "Delete" options for comment available for everyone
    - **Description**: On launch, the "Edit" and "Delete" options for every comment was available for everyone. This was due to a error in the if statement of the template checking the user. It check if the user matched the "comment.commenter" when it should have been checking against "comment.user".
    - **Fix**: Edit template to check for "comment.user"

- Accessing profile:
    - **Issue**: Unable to access user profiles
    - **Description**: Following changes to the order model when integrating Stripe webshooks, users were unable to access their profiles and user accounts were unable to be altered in admin. This was due to migrations not being done on the live site.
    - **Fix**: Migrated tables on the live site.

- Stock:
    - **Issue**: Users able to add more items than in stock
    - **Description**: When users added the maximum amount of stock to their cart, they were able to reload the page and even with 0 quantity of a product variant in stock they could add to their cart (but only 1 item). This was due to the "Add To Cart" button not being disabled when a variant was selected.
    - **Fix**: Edit script to check for and disable "Add To Cart" when stock is 0

### Known Bugs
There are currently no known bugs.