# FlyWheel rent a car

Fly-Wheel Rent a Car is a premier luxury car rental service that also offers a selection of standard vehicles, catering to diverse customer needs. 

 Users can effortlessly browse available cars, select their desired dates and locations, and create bookings through this user-friendly platform. Fly-Wheel Rent a Car delivers unparalleled quality and convenience.

![FlyWheel rent a car](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717429891/Royal%20Drive/readme/all-devices-black_wc3cdy.png)

The live site is available here: [Flywheel Rent a car](https://fly-wheel-rent-c4406dadb89b.herokuapp.com/).

# Table of Contents
- [Features](#features)

# Features
## General

This section discusses the more generic features available throughout the site for all users of the website.

### Navigation Bar
<details>
<summary>Navigation Bar</summary>

![Navbar](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717438731/Royal%20Drive/readme/NavBar_oeuhha.png)
</details>

The navigation bar is featured across all pages. The navbar is a slightly modified version of the Bootstrap's navbar documentation. It includes Navigation button to Home, About Us, contact, car serach, signup and login pages. If the User is logged in then the signup and login button rplaced with profile and logou buttons. It also features the website's logo and a Name on the left corner.

The logo in the navbar is visible on all sized screens and links to the home page as user's expect so that it is quick and easy to return to the index from any page on the site.

The profile button is displayed as the user's name. When clicked, it acts as a drop-down menu, revealing two additional links: one for viewing the profile and another for updating profile details. If the user is a super user, an additional 'Data Management' button is available. This button allows super users to manage the database, including adding city and car details.

The "Rent a Car" button navigates the user to the car search page, but only if the user is logged in. If the user is not logged in, it redirects to a login or signup page. This page provides two navigation options: "Login" and "Signup." Users with an existing account can log in, while new users need to sign up for an account.


### Footer
<details>
<summary>Footer</summary>

![Footer](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717438737/Royal%20Drive/readme/Footer_aecjjh.png)
</details>

The footer is featured across all pages on the website. It includes 6 simple sections related to customer communication, offering ways for the customer to communicate with the business.

1. Explore Us: This section includes navigation links to various pages such as Home, About Us, Contact, and Rent a Car.
2. Meet Us: This section displays the company's address.
3. Reach Us: This section contains the company's phone number and email address.
4. Connect with Us: This section provides links to social media sites like Facebook, Instagram, and YouTube.
5. Subscribe: This feature allows users to receive newsletters by providing their email address.
6. Privacy Policy and Copyright: Located at the bottom of the page, this section includes links to the privacy policy and copyright details.


### Index Page
<details>
<summary>Index Page</summary>

![Index](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717441729/Royal%20Drive/readme/index_mlwwkx.png)
</details>

On the index (home) page, the top of the page features an eye-catching car image designed to immediately grab the user's attention. Accompanying this image is a button that navigates to the car search page, accessible only if the user is logged in. Following this, a paragraph provides an introduction to the company, highlighting its mission and services.

A large, colorful logo of the company is prominently displayed, adding vibrancy and a distinctive identity to the website. The home page is further enhanced with photos of happy customers, aiming to build confidence and trust in new users considering renting from the website.

<details>
<summary>Logos</summary>

![Index](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717441742/Royal%20Drive/readme/logos_igfqdt.png)
</details>

Additionally, there is an animated carousel showcasing the logos of various luxury car brands available for rent through the company. This continuously running carousel underscores the wide range of high-end vehicles on offer.

<details>
<summary>FAQ</summary>

![Index](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717441746/Royal%20Drive/readme/FAQ_ulqfcw.png)
</details>

Towards the bottom of the page, a FAQ section is available, presenting frequently asked questions along with their answers. This section is designed to help customers quickly find information and resolve common queries, enhancing their overall experience on the site.

Overall, the index page is intended to be engaging, informative without overwhelming the customer, and to encourage the user to explore the website further.

### Contact Page
<details>
<summary>About Us</summary>

![About](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717442311/Royal%20Drive/readme/AboutUs_ojtbnv.png)
</details>

On the About Us page, visitors can find a detailed overview of the company's history, services, and key features. The history section offers a brief yet comprehensive narrative of the company's journey, highlighting significant milestones and achievements that have shaped its growth and reputation in the car rental industry.

To enhance user convenience, there is a prominently placed button on the About Us page that directs visitors to the car search page. This allows customers who are inspired by the company's story and offerings to easily proceed with booking a vehicle, streamlining their user experience and facilitating quick access to the rental process.

### Contact Page
<details>
<summary>Contact Us</summary>

![Contact](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717442310/Royal%20Drive/readme/contact_nimefq.png)
</details>


On the Contact page, there is a form designed for quick and easy communication with the company. The form requires minimal input fields, including the user's name, mobile number, email address, and a message. This allows users to directly send messages to the company without needing to open their email or make a phone call.

Upon successfully sending a message, users receive an on-screen confirmation message, informing them that their message has been successfully sent. This immediate feedback ensures users know their communication has been received, enhancing their experience and ensuring they feel heard by the company.


### Privacy Policy
<details>
<summary>Privacy Policy</summary>

![Privacy Policy](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717443125/Royal%20Drive/readme/Privacy_xlkrnd.png)
</details>

In the footer, there is a "Privacy Policy" button that navigates to a new window displaying the company's privacy policy. This feature ensures that users can easily access and review the privacy policy details, providing transparency about how their data is handled and protected by the company.

 It is a simple privacy policy generated with [Privacy Policy Generator](https://www.privacypolicygenerator.info/).

### Subscription
<details>
<summary>Subscription</summary>

![Privacy Policy](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717443124/Royal%20Drive/readme/Subscription_ybivxy.png)
</details>

In the footer, another feature is a subscription form consisting of a single input field for the user's email address. Customers can opt to provide their email address if they wish to receive updates from the company, such as special offers and important news. This subscription option allows users to stay informed about the latest promotions and announcements directly from the company, enhancing their engagement and providing value-added communication.

 This feature is generated with [MailChimp](https://mailchimp.com/?currency=EUR).


## User Authentication

This section discusses features related to the user authentication.

Django allauth was used for user authentication for this website and so functionality for registration and authentication is handled by allauth. The templates used for registration, login/logout, and email confirmation are allauth templates which have been styled to match the rest of the website.

### Registration
<details>
<summary>Signup</summary>

![Signup](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717497118/Royal%20Drive/readme/SignUp_fp9usl.png)
</details>

Registration is accessed through the "Signup" link in the navbar and is necessary for most functionality on the website. A user can complete a purchase and generate a successful order only after registering

Once successfully completed, the user is redirected to the page in the image below where they are informed that a verification has been sent to their email address.

<details>
<summary>Verification Sent</summary>

![Verification Sent](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717497607/Royal%20Drive/readme/verify_message_wbxljj.png)
</details>

<details>
<summary>Verification Email</summary>

![Verification Inbox](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717498224/Royal%20Drive/readme/Screenshot_2024-06-04_at_11.49.33_2_fkrknj.png)

![Verification Email](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717498482/Royal%20Drive/readme/varification_email_oxhal9.png)
</details>

Following the link in the email above, the user is brought to the confirmation page where they can confirm their email address and then are able to login to their profile. When a user successful registers with the site and logs in for the first time, a user profile is created for them in a one-to-one relationship.

<details>
<summary>Confirm Email</summary>

![Confirm Email](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717498636/Royal%20Drive/readme/Email_Confirm_page_av8enn.png)
</details>

After confirming their email, the user is redirected to the login page with the message "You have confirmed your email."

<details>
<summary>Email Confirmed</summary>

![Login Confirmed](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717498874/Royal%20Drive/readme/After_confirm_email_wbx8os.png)
</details>


### Login
<details>
<summary>Login</summary>

![Login](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717497118/Royal%20Drive/readme/Login_eljr0z.png)
</details>

The login page is accessed through a "Login" link from the navbar and the template is standard from allauth and accepts either the user's username or email and their password as valid credentials to login. 

Upon logging in, the user is redirected to the home page with a success message.

<details>
<summary>Login with success meaage</summary>

![Login](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717499334/Royal%20Drive/readme/login_with_a_message_alsq0g.png)
</details>

### Logout
<details>
<summary>Logout</summary>

![Logout](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717499334/Royal%20Drive/readme/logout_kpexmz.png)
</details>

When a user is logged in, the log out page is accessed through a "Logout" link in the navbar. Again, this is a standard allauth template styled to match the rest of the website.


## Rent a Car

This section consists of four main parts: searching for cars, filter cars, viewing car details, and the checkout process.

### Search Cars
<details>
<summary>Car search form</summary>

![Car search form](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717500644/Royal%20Drive/readme/Search_cars_Form_xdwet7.png)
</details>

Using the car search form, the user can input pickup and drop-off details, including location, date, and time. The user will then be redirected to a collection of available cars at the selected pickup location and date. If no cars are available, a message will prompt the user to choose a car from a different location or date.

<details>
<summary>Search result with cars</summary>

![Search result with cars](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717501394/Royal%20Drive/readme/search_result_with_cars_hvzjgr.png)
</details>

<details>
<summary>Search result without cars</summary>

![Search result without cars](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717501394/Royal%20Drive/readme/Search_result_without_car_vx3fur.png)
</details>

### Filter Cars

If the customer wants to filter the cars by specific features such as category, fuel type, number of seats, or gearbox type, they can use the filter options on the search results page. Additionally, if the customer needs to change the pickup and drop-off details, this can also be done using the filter form. The filter options provide a convenient way to refine search results to match the customer's preferences and requirements, ensuring they find the most suitable car for their needs.

<details>
<summary>Filter form</summary>

![Filter form](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717501903/Royal%20Drive/readme/Filter_Form_ghs8pm.png)
</details>

### Choose a Car

If the customer finds a car that meets their needs or wants to learn more about a specific car, they can click the "View Deal" button associated with each car. This action will redirect the customer to the car details page, where they can view comprehensive information about the car.

<details>
<summary>Car details</summary>

![Car details](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717502332/Royal%20Drive/readme/car_details_wmlhpb.png)
</details>

On the car details page, there are three main sections of information:

1. Pickup and Drop-off Details:

    This section displays the pickup and drop-off details selected by the customer, including the locations, dates, and times.

2. Car Details:

    This section provides comprehensive information about the car, such as its category, fuel type, number of seats, gearbox type, and other relevant features.
3. Rent Calculation and Grand Total:

    This section shows the calculations of the rental cost, including the breakdown of daily rates and the grand total.

Additionally, there is an extra section where the customer can choose to add optional items such as booster seats, child seats, and infant car capsules. If the customer opts for any of these extras, the additional costs are automatically calculated and added to the grand total, which is updated and displayed in the calculation area. This ensures that the customer has a clear understanding of the total cost, including any extras they choose to add.

<details>
<summary>Extras</summary>

![Extras](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717502862/Royal%20Drive/readme/extras_cm18ko.png)
</details>

On the car details page, there is a dedicated section to provide important information to the customer, ensuring they arrive on time and fully prepared for pickup. This section includes details such as:

1. Arrival Information:

    Instructions on how to arrive on time at the pickup location, including any specific directions or landmarks.
2. What to Bring:

    A checklist of items that the customer should bring with them when coming to pick up the car, such as a valid driver's license, proof of insurance, and any necessary payment methods.
3. Refundable Deposit Details:

    Information regarding the refundable deposit amount, including the accepted payment methods and any conditions for refunding the deposit upon return of the car.


<details>
<summary>Pickup checklist</summary>

![Pickup checklist](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717503688/Royal%20Drive/readme/terms_and_conditions_vlrico.png)
</details>

Additionally, there is a "Terms and Conditions" button that allows the customer to navigate to the terms and conditions page for further information about rental policies, responsibilities, and agreements. This ensures transparency and clarity regarding the terms of the rental agreement, helping customers make informed decisions.

<details>
<summary>Terms and conditions</summary>

![terms and conditions](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717503988/Royal%20Drive/readme/terms_and_conditions_kc5idl.png)
</details>

If the user does not find a car that meets their needs, they can return to the same search results page with all the filters they previously applied. This can be done by clicking the "Change Car" button at the top of the car details section. This feature ensures a seamless experience by preserving the user's search criteria, making it easy to explore other available options without having to reapply filters.

If the customer wants to rent the car, they can click on the "Checkout" button to proceed with the payment. This action will guide the customer through the necessary steps to complete the rental process, ensuring a smooth and secure transaction.

### Checkout

In the checkout page, there are two main sections:

1. Booking Details:

    This section displays information about the pickup and drop-off locations, rental duration, selected extras, and the grand total cost. It provides a summary of the booking details for the customer's review before proceeding to payment.
2. Checkout Form:

    This section collects the customer's billing details, including their name, address, and contact information. Additionally, it prompts the customer to provide their driver's license and personal ID details, as well as their payment information, such as credit card details.

If the customer has already updated their personal details in their profile, the form will be automatically filled with those details, allowing the customer to review and make any necessary changes. If the customer has not previously updated their personal details, the information entered in the billing details section will be stored as their personal details.

If the customer needs to update their personal details in the future, they can do so through the profile page. This ensures that the customer's information is always current and can be easily managed. 

<details>
<summary>Checkout page</summary>

![checkout page](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717504958/Royal%20Drive/readme/checkout_page_sinljn.png)
</details>

Once the customer fills in all the required details and clicks the "Book and Pay" button, a booking will be created, and they will be redirected to the checkout success page. This page confirms that the booking has been successfully processed and provides any relevant information regarding the reservation.

<details>
<summary>Checkout success page</summary>

![checkout success page](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717505111/Royal%20Drive/readme/checkout_success_page_hou8ah.png)
</details>

When the booking is successful, an email confirmation will be sent to the provided email address with the appropriate details about the booking. This email will include information such as the pickup and drop-off locations, dates and times, car details,  and the grand total. The confirmation email helps the user understand and review their booking details, ensuring they have the necessary information readily available.

<details>
<summary>Bookin confirmation e mail</summary>

![Bookin confirmation e mail](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717506285/Royal%20Drive/readme/Booking_Confirmation_e_mail_tflfwq.png)
</details>

#### Stripe

The payment gateway is integrated using [Stripe](https://stripe.com/ie). This ensures secure and reliable processing of credit/debit card payments.


## Profile

This section is divided for two categories of users: normal users (customers) and super users. When logged in, the user's username appears as a dropdown button in the navigation bar.

### User

If the user is a customer, the dropdown menu provides the following options:
    
1. Profile: Redirects the user to their profile page, where they can view their personal information, booking history, and other relevant details.
2. Update Profile: Allows the user to update their personal details, such as their name, email address, phone number, and billing information. This ensures that all personal information is current and accurate for future bookings.

### Super User
Super users, typically administrators or staff with higher privileges, have an additional option in their dropdown menu:
1. Data Management: This section provides tools for super users to manage the system's data. They can add or delete car details, such as model, make, category, and availability. They can also manage city details.

 This feature is essential for keeping the rental service's database up to date, ensuring that customers have accurate and comprehensive options to choose from.

<details>
<summary>Profile menu</summary>

![Profile menu](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717507593/Royal%20Drive/readme/profile_menu_ls0pq2.png)
</details>