Documentation
sharing_is_caring
Simeon Rangelov - MrSims

Table of Contents
1 Introduction

2 Product Overview

2.1 Product Features
2.2 User Characteristics
2.3 Profile objects
2.4 Recipe objects
2.5 Ingredient objects
3 Additional Sevices

3.1 Claudianry
4 Requirements Met

4.1 Mandatory Requirements
4.2 Optional Requirements


1. Introduction
The purpose of this document is to present a description of the Web Project. It will explain the purpose and features of the system, the interfaces of the system, what the system will do.

2. Product Overview
the sharing_is_caring app is developed to help direct exchange of baby and toddler oriented goods. Those who have more can easily find those who have few and vice versa.

2.1 Product Features
Custom user authentication profile with auto-generated user profile that holds personal info  
Create, read, update, delete posts after filling out all needed user profile data
View other user profilea and comment oon them after filling out all needed user profile data

2.2 User Characteristics
User can sign-in with email and password. 

2.2.1 Admin User
The admin user gets enabled through the admin site by another admin user, setting their 'is_staff' field to True.

This user has all CRUD permissions over other users, their profiles and all recipes in the database. After authentication this user can access the admin site through the top navigation panel.

2.3 Profile Objects
Profile is auto-created on user creation with user_id same is user.id.
The user profile has first name, last name, city, address, gender, image, number of children and all CRUD operations related to it.
This user has all CRUD permissions to their own posts. They comment all other users profiles in the system.

Components:
User - OneToOne-relation with the user
First name - Charfield
Last name - Charfield
Address - Charfield
City - Charfield
Number of children - PositiveIntegerfield
Gender - Charfield with choices(Male, Female)
Image - Imagefield

Comments - set of comment objects related with a foreign-key to the recipe


2.4 Post Objects
The Recipe object could be either public or private. It can be viewed by all types of users, but created, edited and deleted only by its author.

Components:
user - Foreignkey relation with the user
Name - Charfield
ItemType - Charfield with choices(Toy, Clothes, Tool)
Condition - Charfield with choices(New, Used, Used with problems)
Type - Charfield with choices(Searching, Give-Away)
Image - Imagefield


4. Requirements Met

4.1 Mandatory requirements / Must haves
 The application must be implemented using Django Framework
 The application must have at least 10 endpoints
 The application must have login/register functionality
 The application must have public part (A part of the website, which is accessible by everyone – un/authenticated users and admins)
 The application must have private part (accessible only by authenticated user and admins)
 The application must have admin part (accessible only to admins)
 Unauthenticated users (public part) have only 'get' permissions e.g., landing page, details, about page
 Authenticated users (private part) have full CRUD for all their created content
 Admins have full CRUD functionalities
 Form validations
 To avoid crashes, implement Error Handling and Data Validations
 Use PostgreSQL as a database.
 Write tests for at least 60% coverage on your business logic
 Templates (your controllers/views must return HTML files) – one and the same template could be re-used/used multiple times (with the according adjustments, if such needed)
 Use a source control system by choice – Github or Gitlab. You must have at least 5 commits + README

4.2 Optional / Bonuses
 Responsive web design
 Class-based views
 Extended Django user
 Documentation/ Swagger
