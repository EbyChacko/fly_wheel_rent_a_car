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

### Profile Page

In the profile section, there are two main areas:

<details>
<summary>Profile page without booking</summary>

![Profile page without booking](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717510269/Royal%20Drive/readme/profile_without_booking_uefdat.png)
</details>

#### Personal Details:

- This section displays the user's personal information, such as their name, email address, phone number, address and date of birth.
- Users can review their details and ensure that all information is up-to-date.
- There is an option to edit and update these details, allowing users to keep their profile current.

For users who wish to modify their personal information, a dedicated "Update Profile" button will be located within the "Personal Details" section. Clicking this button will direct them to a "Update Personal Details" page. This dedicated page will provide a user-friendly form, allowing them to effortlessly modify their personal information.

The same form can be accessed by clicking the "Update Profile" button in the drop down menu in the user name button.

<details>
<summary>Update Profile form</summary>

![Update Profile form](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717512179/Royal%20Drive/readme/update_profile_form_th7tdn.png)
</details>

#### List of Bookings:

- This section provides an overview of the user's booking history.
- Each booking entry includes details such as the car model, pickup and drop-off locations, dates, times, and the status of the booking (e.g., Booked or canceled).
- Users can click on individual bookings to view more detailed information, including rental costs, selected extras, and any applicable terms and conditions.
- This section helps users keep track of their past and upcoming rentals, providing easy access to all relevant booking information.

    To make it easier to understand the status of each booking, different background colors are used for different booking statuses. 

    For example: 
    - Green for booked
    - Dark pink for canceled

    <details>
    <summary>Profile page with bookings</summary>

    ![Profile page with bookings](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717510848/Royal%20Drive/readme/Profile_page_with_booking_owlbcx.png)
    </details>

These two sections ensure that users have a comprehensive view of their personal information and booking history, enhancing their overall experience with the rental service.

### Booking details


To view the specifics of a booking, users can simply click the "View Details" button associated with that booking. This action will direct them to a dedicated booking details page. This page will provide a clear overview of all relevant booking informations same as the the car details page, with added information about the billing details and the licence and personal id details.

<details>
<summary>Booking Details</summary>

![Booking Details](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717513051/Royal%20Drive/readme/Booking_details_r4wash.png)
</details>

At the bottom of the page, you'll find two options: "Cancel Booking" and "Delete Booking".

1. Cancel Booking: 
    
    Clicking "Cancel Booking" redirect to the confirm cancel page. if the customer choose cancel again, it will change the booking status to "Canceled." You'll then be redirected back to your profile page with a successful message. Canceled bookings remain accessible for your reference and will display a "Canceled" status.
    <details>
    <summary>Cancel Booking confirmation  Page</summary>

    ![Cancel Booking confirmation  Page](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717514026/Royal%20Drive/readme/Cancel_Booking_yfbjlm.png)
    </details>

2. Delete Booking: 

    Selecting "Delete Booking" redirect to the confirm cancel page. if the customer choose cancel again, it will permanently remove the booking from the user profile. Once deleted, the user won't be able to see the booking details. However, administrators can still access deleted bookings through the admin panel with a "Deleted" status.
    <details>
    <summary>Delete Booking confirmation Page</summary>

    ![Delete Booking confirmation Page](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717514026/Royal%20Drive/readme/Delete_Booking_skvkdl.png)
    </details>

### Data Management

The data management page is accessible through the dropdown menu under the username button in the navbar by only the super user. This page offers functionalities for managing both cities and cars.

<details>
<summary>Data Management page</summary>

![Data Management page](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717515995/Royal%20Drive/readme/data_management_umrnza.png)
</details>



1. City management:

    the user can see a list of all currently added cities.
    <details>
    <summary>city List</summary>

    ![city List](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717515993/Royal%20Drive/readme/city_list_m6v7z6.png)
    </details>

    - Adding a new city is as simple as clicking the "Add City" button. A form will then appear on the same page, allowing the user to enter the city name and its corresponding county.
        <details>
        <summary>Add city form</summary>

        ![Add city form](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717515992/Royal%20Drive/readme/add_city_form_iwp9r7.png)
        </details>

    - To remove a city, you can click the "Delete" button next to its name. However, keep in mind that this action will take you to a confirmation page, and choosing "Delete" permanently removes the city from the system and redirected to the car lists with a success message.

        <details>
        <summary>Remove City confirm page</summary>

        ![Remove City confirm page](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717516366/Royal%20Drive/readme/remove_city_n901ju.png)
        </details>

2. Car management:
    It follows a similar structure. You'll find a list of existing cars.
    <details>
    <summary>Car List</summary>

    ![Car List](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717515992/Royal%20Drive/readme/car_list_vttukf.png)
    </details>

    - To add City: There will be an "Add Car" button for new entries. Clicking this button will display a form where you can enter all the relevant car details. 
        <details>
        <summary>Add Car form</summary>

        ![Add Car form](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717515991/Royal%20Drive/readme/add_car_form_maggio.png)
        </details>

    - To delete Car, each car listing has a "Delete" button. Clicking it leads to a confirmation page, and confirming deletion will permanently remove the car information from the database and redirected to the car lists with a success message.

        <details>
        <summary>Remove car confirm page</summary>

        ![Remove car confirm page](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717515996/Royal%20Drive/readme/remove_car_lavv1m.png)
        </details>



## Admin

Most of the functionality available on the main website to staff users is also available through the admin panel. All the models are registered to allow admin users to perform CRUD functionality through the admin panel.

In some cases CRUD functionality is only available through the admin panel. For example, "Title" are registered with admin but there's no functionality available through the management dashboard on the main site. 

Similarly, users and user profiles can be managed through the admin panel, including deleting users, but this functionality is not present on the management dashboard to discourage staff from attempting to manipulate the user database. Users are able to edit their own profile details or delete their account themselves, but these options are available to them through their profile as they have the right to manage their own personal information.


## Future Features

1. __Improved data Management__:
    - Data management can be improved to allow users more control on data management. 
2. __Book Again__:
    - For registered users you could offer an "Book Again" button for the car in their booking history. This could be as simple as clicking the button to create booking bu just doing the checkout.
3. __Creating a PDF Bill__: 
    - When the user creates a booking, The user want recieve a PDF formated bill in the mail and can be downloaded from the website(in the booking details page).
4. __Booking management by the super user__:
    - The super user can update the details of a booking if the booking need any updations. Now this feature is available only in the admin panel. 


# Agile Methodology
## Epics, User Stories

The project board can be found [here](https://github.com/users/EbyChacko/projects/6).


# Design

## Colour

The 90 % of the project is done using the black background. And the letters are white.
Most of the colouring are done using the bootstrap colours.

1. Black
2. Dark
3. Secondary
4. Warning
5. Info
6. White


Additionally in the CSS I have use the following colours. Some of them are used as reduced transparency in the website.
<details>
<summary>Colour Palette</summary>

![Colour Palette](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717519524/Royal%20Drive/readme/Colour_pallet_oeh0di.png)
</details>

## Wireframes

Wireframes were created using [Figma](https://www.figma.com). They were created for initial planning for the layout of the website.

<details>
<summary>Index</summary>

![Index](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717437200/Royal%20Drive/readme/Flywheel_Wireframe_0_xnfpx6.jpg)
</details>

<details>
<summary>Contact</summary>

![Contact](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717437200/Royal%20Drive/readme/Flywheel_Wireframe_2_kheou0.jpg)
</details>

<details>
<summary>About Us</summary>

![About Us](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717437201/Royal%20Drive/readme/Flywheel_Wireframe_1_rahmdt.jpg)
</details>

<details>
<summary>Search car Form</summary>

![Search car Form](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717437199/Royal%20Drive/readme/Flywheel_Wireframe_3_facxca.jpg)
</details>

<details>
<summary>Search result</summary>

![Search result](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717437199/Royal%20Drive/readme/Flywheel_Wireframe_4_ef0mfd.jpg)
</details>

<details>
<summary>Car details</summary>

![Car details](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717437199/Royal%20Drive/readme/Flywheel_Wireframe_5_pnswwm.jpg)
</details>

<details>
<summary>Checkout</summary>

![Checkout](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717437200/Royal%20Drive/readme/Flywheel_Wireframe_6_gxhkw6.jpg)
</details>

<details>
<summary>Profile</summary>

![Profile](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717437201/Royal%20Drive/readme/Flywheel_Wireframe_7_gz5ehp.jpg)
</details>

<details>
<summary>Bokking Details</summary>

![Bokking Details](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717437200/Royal%20Drive/readme/Flywheel_Wireframe_8_gudzvh.jpg)
</details>



## Entity Relationship Diagrams

ER diagram is created using the [dbdiagram.io](https://dbdiagram.io/)
<details>
<summary>ERD</summary>

![ERD](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717529044/Royal%20Drive/readme/ER_Diagram_rjstl1.png)
</details>

<br>

## Flow chart

The flow chart is created using the [figma.com](https://figma.com/)
<details>
<summary>Flow Chart</summary>

![Flow Chart](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717535678/Royal%20Drive/readme/Flywheel_Rent_a_car_flow_chart_digram_1_y3sske.png)
</details>

<br>

# SEO and Marketing

## SEO, Keywords

Based on the Institute's SEO video, I have compiled a list of key terms. Using [Wordtracker](https://www.wordtracker.com/), I discovered the following keywords to be the most effective for optimizing the website's SEO:
- car rentals
- Auto rentals near me
- premium car rental
- Luxuary car rental
- affordable car rental

Some of the searches are given below.
<details>
<summary>affordable car rental</summary>

![affordable car rental](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717530703/Royal%20Drive/readme/SEO_4_gerhkp.png)
</details>

<details>
<summary>Premium car rental</summary>

![Premium car rental](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717530702/Royal%20Drive/readme/SEO_3_eeoses.png)
</details>


<details>
<summary>car rental</summary>

![car rental](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717530702/Royal%20Drive/readme/SEO_1_jaj1pe.png)
</details>


<details>
<summary>auto rentals near me</summary>

![auto rentsls near me](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717530701/Royal%20Drive/readme/SEO_2_xfsaof.png)
</details>


## Marketing
Based on Code Institute's Web Marketing, questions were collected to try to decide on marketing for the website.

- What kind of business is it?
  - B2C
- Who are your customers?
  - High-end clientele looking for premium car rental experiences
  - Includes business travelers, vacationers, and car enthusiasts
- Which online platforms would you find lots of your users?
  - Social media platforms like Instagram, Facebook, and YouTube to showcase fleet and lifestyle content
  - Luxury travel blogs and magazines to reach affluent travelers
  - Car enthusiast forums and websites to connect with car lovers
- What do your users need?
  - Large collection of premium luxuary cars
- Would your business run sales or offer discounts? How do you think your users would most like to hear about these offers?
  - Sales and discounts could be offered. Either through posting alerts for sales on social media or sending discount codes to people on the newsletter.
- Would your business have a budget to spend on advertising? Or would it need to work with free or low cost options to market itself?
  - Possibly a small budget. It would start with low cost options like social media and newsletters.

The e-commerce businesses that inspired aspects of this website include:
  - [rentalcars.com](https://www.rentalcars.com/)


## Social Media


Above is a mock up of the Facebook business page for the Flywheel. This would be the primary social media site for the business to communicate with customers.


<details>
<summary>Facebook page 1</summary>

![Facebook page](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717532266/Royal%20Drive/readme/fb-3_fycheg.png)
</details>

<details>
<summary>Facebook page 2</summary>

![Facebook page](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717532265/Royal%20Drive/readme/fb-2_jn49yq.png)
</details>


<details>
<summary>Facebook Add</summary>

![Facebook add](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717532267/Royal%20Drive/readme/fb-1_sqv481.png)
</details>

<br>
Instagram and YouTube should be consider with site expansion as Flywheel is getting popular.


I am glad to inform that the Facebook page has been noticed by someone, and a customer has inquired about car rentals. The Facebook chat is given below.

<details>
<summary>Facebook chat with customer</summary>

![Facebook chat](https://res.cloudinary.com/dgd5gtn1w/image/upload/v1717531966/Royal%20Drive/readme/Screenshot_2024-06-04_at_21.11.43_2_sx7qk1.png)
</details>

## Email

Through a subscription form in the footer, the website implements newsletter using Mailchimp. The intention with the newsletter would be to update customers when new cars are arrived or new offers are launched.


# Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5): mark-up language.
- [CSS3](https://en.wikipedia.org/wiki/CSS): styling.
- [JavaScript](https://www.javascript.com/): programming language.
- [Python 3](https://www.python.org/): programming language.
- [Django 3.2](https://www.djangoproject.com/)
  - [Django allath](https://django-allauth.readthedocs.io/en/latest/index.html): user authentication.
  - [widget tweaks](https://pypi.org/project/django-widget-tweaks/): for forms.
  - [Django countries](https://pypi.org/project/django-countries/): for countries in forms.
  - [Pillow](https://pypi.org/project/Pillow/): python imagining library.
- [Stripe](https://stripe.com): payments.
- [JQuery](https://jquery.com/)
- [Bootstrap](https://getbootstrap.com/): styling.
- [Cloudinary](https://cloudinary.com/): store static and media files.
- [GIT](https://git-scm.com/): for version control.
- [GitHub](https://github.com/): for host repository.
- [Gitpod](https://www.gitpod.io/): online IDE.
- [Heroku](https://heroku.com/): deployment
- [Google Fonts](https://fonts.google.com/): to import fonts.
- [Font Awesome](https://fontawesome.com/): to import icons.
- [figma](https://www.figma.com/): to create wireframes.
- [dbdiagram.io](https://dbdiagram.io/home): for Entity Relationship Diagram.
- [Photoshop](https://www.gimp.org/): to edit images and create logo
- [Coolers](https://coolors.co/): create colour palette.



# Testing

Testing for the site can be found at the below link:

[Link to TESTING.md](TESTING.md)


# Deployment

## Steps to deploy site using Heroku:
- Assuming gunicorn, dj_database_url, psycopg2 and django-cloudinary-storage have been installed
- Create an external database with ElephantSQL
  - Register/login to your ElephantSQL dashboard and click "Create New Instance"
  - Select a name and plan for your database
  - Then click "Select Region"
  - Select a region and data center close to you
  - Click "Review", then check your details are correct and click "Create Instance"
  - Select the database from your dashboard and you can see the URL for your database
- On the Heroku dashboard, select "New" and click "Create new app"
  - Create a unique app name - this will be added to allowed hosts in the project settings
  - Select your region
  - Click "Create app"
- Go to the Resources tab:
  - Search for "postgres" in the add-ons search bar and select "Heroku Postgres"
  - Click "Submit Order Form"
- Go to the settings tab:
  - Scroll down to the config vars section and select "Reveal Config Vars"
  - Add a new config var for DATABASE_URL - copy the URL from your ElephantSQL database that you created earlier
  - Add a new config var for SECRET_KEY - create your own or use a django secret key generator
  - Add a new config var for CLOUDINARY_URL - copy the "API Environment variable" from your cloudinary dashboard, do not include "CLOUDINARY_URL="
  - Add a new config var for STRIPE_PUBLIC_KEY - copy your public key from stripe
  - Add a new config var for STRIPE_SECRET_KEY - copy your secret key from stripe
  - Add a new config var for STRIPE_WH_SECRET - copy your webhook secret from stripe from when you connected your endpoint
  - Add a new config var for EMAIL_HOST_USER - enter the gmail address you're using for this project
  - Add a new config var for EMAIL_HOST_PASS - enter the 16 digit key gmail app password
  - Add a new config var for DISABLE_COLLECTSTATIC, with the value 1 - this will be removed before deployment
- In your project, for your environment variables:
  - Create a new env.py file in the top level directory
  - In env.py:
    - Import os
    - Add 'os.environ["DATABASE_URL"] = "Paste the DATABASE_URL from the Heroku app here"'
    - Add 'os.environ["SECRET_KEY"] = "Paste your new secret key here"'
    - Add 'os.environ["CLOUDINARY_URL"] = "Paste your CLOUDINARY_URL as in the Heroku app here"'
    - Add 'os.environ["STRIPE_PUBLIC_KEY"] = "Paste your STRIPE_PUBLIC_KEY here"' - this isn't required to be secret, but for sake of keeping these keys together
    - Add 'os.environ["STRIPE_SECRET_KEY"] = "Paste your STRIPE_SECRET_KEY here"'
    - Add 'os.environ["STRIPE_WH_SECRET"] = "Paste your STRIPE_WH_SECRET here"'
  ```
  import os

  os.environ['DATABASE_URL'] = 'postgres://exampledatabaseurl'
  os.environ['SECRET_KEY'] = 'examplesecretkey'
  os.environ['CLOUDINARY_URL'] = 'cloudinary://examplecloudinaryurl'
  os.environ['STRIPE_PUBLIC_KEY'] = 'examplestripepublickey'
  os.environ['STRIPE_SECRET_KEY'] = 'examplestripesecretkey'
  os.environ['STRIPE_WH_SECRET'] = 'examplestripeWHsecret'
  ```
  - If not already present, create a .gitignore file and add env.py to it

- In your project, in settings.py:
  - Import os
  - Import dj_database_url
  - if os.path.isfile('env.py'):
	import env
  ```
  import os
  import dj_database_url
  if os.path.isfile('env.py'):
      import env
  ```
  - Replace the insecure secret key with "SECRET_KEY = os.environ.get('SECRET_KEY')"
  ```
  SECRET_KEY = os.environ.get('SECRET_KEY')
  ```
  - Link new database by commenting out old DATABASES section and adding:
	DATABASES = {
			'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
			}
  ```
  DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
  ```
  - Add Heroku to the allowed hosts: "ALLOWED_HOSTS = ['the_app_name_from_heroku.herokuapp.com']
  ```
  ALLOWED_HOSTS = ['example-heroku-app-name.herokuapp.com', 'localhost']
  ```
  - Add 'cloudinary_storage' (above 'django.contrib.staticfiles') and 'cloudinary' (below) to INSTALLED_APPS
  ```
  ...
  'cloudinary_storage',
  'django.contrib.staticfiles',
  'cloudinary',
  ...
  ```
  - Setup Cloudinary to store static and media files
  ```
    STATIC_URL = '/static/'
	STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
	STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
	STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

	MEDIA_URL = '/media/'
	DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
  ```
  - Run 'python3 manage.py collectstatic' to collect static files
- In your project:
  - Create a Procfile in the top level directory and add 'web: gunicorn project_name.wsgi' to tell 
  ```
  web: gunicorn project_name.wsgi
  ```
  - Create a requirements file with 'pip3 freeze --local > requirements.txt' for Heroku to install required packages
  ```
  pip3 freeze --local > requirements.txt
  ```
  - Make migrations with 'python3 manage.py migrate'
  ```
  python3 manage.py migrate
  ```
  - Commit and push to GitHub
- Prior to final deployment:
  - Set DEBUG = False in project settings.py
  - Remove DISABLE_COLLECTSTATIC config var from Heroku
- Go to the Deploy tab:
  - Select GitHub and confirm connection to GitHub account
  - Search for the repository and click "Connect"
  - Scroll down to the deploy options
  - Select automatic deploys if you would like automatic deployment with each new push to the GitHub repository
  - In manual deploy, select which branch to deploy and click "Deploy Branch"
  - Heroku will start building the app
- The link to the app can be found at the top of the page by clicking "Open app"

The live site can be found here: [Flywheel Rent a car](https://fly-wheel-rent-c4406dadb89b.herokuapp.com/)

## Steps to clone site:
- In the GitHub repository, click the "Code" button.
- Select "HTTPS" and copy the URL.
- Open Git Bash and navigate to the repository where you would like to locate the cloned repository.
- Type "git clone" followed by the copied URL.
- Press enter to create the clone.
- Install required packages with the command "pip3 install -r requirements.txt"


# Credits
## Code

- The code for srtipe is based on Code Institute's [Boutique ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1)
- The privacy policy and HTML for it is from [Privacy Policy Generator](https://www.privacypolicygenerator.info/)
- logo carousel tutorial from [youtube]( https://www.youtube.com/watch?v=nAjR0Oj0J8E)
- widget Tweaks form styling tutorial from [youtube](https://youtu.be/ynToND_xOAM?si=PBZfE-EeFRJ077ec)

## Media
- Icons are from [Font Awesome](https://fontawesome.com)
- The fonts are imported from [Google Fonts](https://fonts.google.com)

- Images from [Freepik](https://www.freepik.com/):
  - [Logo Image](https://www.freepik.com/free-vector/gradient-car-service-logo-template_32378266.htm#fromView=search&page=1&position=19&uuid=2aa67cec-052e-4c5f-b2ab-fc25ac6a0434)
  - [Home page car image ](https://www.freepik.com/free-vector/lightened-luxury-sedan-car-darkness-with-headlamps-rear-lights-lit-realistic-image-reflection_6867608.htm#fromView=search&page=1&position=0&uuid=d45e76ff-074b-40b6-a3f9-52cbbc8a4ce8)
  - [Car image](https://www.freepik.com/free-vector/lightened-luxury-sedan-car-against-night-city-with-headlamps-rear-tail-lights-lit_6867609.htm#query=black%20car&position=49&from_view=keyword&track=ais&uuid=f10faeb6-30a1-462f-9108-a194663c311e)
  - [About page image 1]( https://www.freepik.com/free-ai-image/photorealistic-happiness-scene-with-happy-woman_171767280.htm#fromView=search&page=1&position=11&uuid=8f4e2c78-d00c-4b47-a0a9-b8c7fffe0fec)
  - [About page image 2](https://www.freepik.com/free-ai-image/summertime-seasonal-scene-with-monochromatic-black-white-effect_138702855.htm#fromView=search&page=1&position=28&uuid=8f4e2c78-d00c-4b47-a0a9-b8c7fffe0fec)
  - [About page image 3](https://www.freepik.com/free-photo/car-dealer-customer-vehicle-showroom-choosing-new-car_11136278.htm#fromView=search&page=1&position=50&uuid=71a30d3d-579b-4062-8b86-2644e49e9a36
  )
  - [Home page customer image](https://www.freepik.com/free-photo/young-woman-holding-car-keys_27091452.htm#fromView=search&page=1&position=38&uuid=88c1ec58-b50e-4832-8dfc-c327b7b71cbf?log-in=google)


- Images from other sourses:
  - [Search page car image ](https://wallpapers.com/images/hd/black-car-4k-w132c4fj1juguqjr.jpg)

## Acknowledgement
I'd like to thank my mentor, Graeme, for providing very good advice, tips and feedback, as well as excellent resources that aided greatly in organising and implementing this project.