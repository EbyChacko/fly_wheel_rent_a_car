# The Chillibox
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

Python validation for PEP8 compliance was performed using [pycodestyle](https://pycodestyle.pycqa.org/en/latest/index.html) to check linting errors. Where appropriate, in a small number of cases "# noqa" was used, especially for "errors" in Django generated files. 

[CI Python Linter](https://pep8ci.herokuapp.com/) was used to double check some pages by copy and pasting code, as a back up to confirm there were no linting issues.

<details>
<summary>Python Problems</summary>

![Problems](readme-docs/testing/python_validation.webp)
</details>


## Automated Testing

Automated testig was performed using Django's testing tools and measured using coverage. The pages of the coverage report are below.

<details>
<summary>Coverage Pg1</summary>

![Coverage 1](readme-docs/testing/coverage_one.webp)
</details>

<details>
<summary>Coverage Pg2</summary>

![Coverage 2](readme-docs/testing/coverage_two.webp)
</details>

<details>
<summary>Coverage Pg3</summary>

![Coverage 3](readme-docs/testing/coverage_three.webp)
</details>


## Manual Testing
Below the steps for manual testing of the site have been arranged into tables. User stories are matched to the manual tests which demonstrate their fulfillment in the User Story column. The User Story numbers can be found on the project board under their Epics or in the main README file under Agile Methodology - Epics & User Stories.

The fulfillment of acceptance criteria for user stories is not the focus of the manual testing as this was documented when features were implemented in comments on each user story on the project board.

<details>
<summary>Manual Testing for User Authentication</summary>

![User Authentication](readme-docs/testing/testing_allauth.webp)
</details>

<details>
<summary>Manual Testing for User Profiles</summary>

![User Profiles](readme-docs/testing/testing_profiles.webp)
</details>

<details>
<summary>Manual Testing for Home</summary>

![Home](readme-docs/testing/testing_home.webp)
</details>

<details>
<summary>Manual Testing for Products</summary>

![Products](readme-docs/testing/testing_products.webp)
</details>

<details>
<summary>Manual Testing for Cart</summary>

![Cart](readme-docs/testing/testing_cart.webp)
</details>

<details>
<summary>Manual Testing for Checkout</summary>

![Checkout](readme-docs/testing/testing_checkout.webp)
</details>

<details>
<summary>Manual Testing for Management Pt1</summary>

![Managment Pt1](readme-docs/testing/testing_management.webp)
</details>

<details>
<summary>Manual Testing for Management Pt2</summary>

![Management Pt2](readme-docs/testing/testing_management_2.webp)
</details>

<details>
<summary>Manual Testing for Recipes</summary>

![Recipes](readme-docs/testing/testing_recipes.webp)
</details>


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