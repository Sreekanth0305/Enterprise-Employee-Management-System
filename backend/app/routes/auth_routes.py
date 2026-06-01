from fastapi import APIRouter

from app.models.auth_model import (
    SignupSchema,
    LoginSchema,
    ForgotPasswordSchema
)

from app.database.users_db import users

auth_router = APIRouter()

# SIGNUP

@auth_router.post("/signup")
def signup(data: SignupSchema):

    existing_user = next(

        (
            user
            for user in users

            if user["email"].lower()
            == data.email.lower()
        ),

        None
    )

    if existing_user:

        return {
            "success": False,
            "message": "Email already exists"
        }

    new_user = {

        "id": len(users) + 1,

        "name": data.name,

        "email": data.email,

        "password": data.password,

        "role": data.role
    }

    users.append(new_user)

    return {

        "success": True,

        "message":
        "Signup Successful"
    }


# LOGIN

@auth_router.post("/login")
def login(data: LoginSchema):

    matched_user = next(

        (
            user
            for user in users

            if user["email"].lower()
            == data.email.lower()

            and user["password"]
            == data.password
        ),

        None
    )

    if matched_user:

        return {

            "success": True,

            "message":
            "Login Successful",

            "role":
            matched_user["role"],

            "user":
            matched_user
        }

    return {

        "success": False,

        "message":
        "Invalid Credentials"
    }


# FORGOT PASSWORD

@auth_router.put("/forgot-password")
def forgot_password(
    data: ForgotPasswordSchema
):

    for user in users:

        if (
            user["email"].lower()
            == data.email.lower()
        ):

            user["password"] = (
                data.new_password
            )

            return {

                "success": True,

                "message":
                "Password Updated Successfully"
            }

    return {

        "success": False,

        "message":
        "User Not Found"
    }