swagger_attendance_spec = {
    "parameters": [
        {
            "name": "semester",
            "in": "query",
            "type": "integer",
            "required": True,
            "description": "Semester for which attendance is requested",
        },
        {
            "name": "Authorization",
            "in": "header",
            "type": "string",
            "required": True,
            "description": "Authorization token to access routes",
        },
    ],
    "responses": {
        200: {
            "description": "Successful response with attendance details",
            "schema": {
                "type": "object",
                "properties": {
                    "university_reg_no": {
                        "type": "string",
                        "description": "University registration number",
                    },
                    "roll_no": {"type": "string", "description": "Roll number"},
                    "name": {"type": "string", "description": "Student name"},
                    # Add properties for each subject attendance dynamically here
                    "total_present_hours": {
                        "type": "string",
                        "description": "Total present hours for all subjects",
                    },
                    "total_hours": {
                        "type": "string",
                        "description": "Total hours for all subjects",
                    },
                    "total_percentage": {
                        "type": "string",
                        "description": "Overall attendance percentage",
                    },
                },
            },
            "examples": {
                "rgb": {
                    "CET415": {
                        "attendance_percentage": "N/A",
                        "present_hours": "0",
                        "total_hours": "0",
                    },
                    "CSD415": {
                        "attendance_percentage": "80%",
                        "present_hours": "16",
                        "total_hours": "20",
                    },
                    "name": "DEVADATHAN M B",
                    "roll_no": "26",
                    "total_hours": "52",
                    "total_percentage": "85%",
                    "total_present_hours": "52",
                    "university_reg_no": "KTE20CS022",
                }
            },
        },
        400: {
            "description": "Bad request. Check the error message for details.",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "Error message"}
                },
            },
        },
        401: {
            "description": "Unauthorized. User needs to log in again.",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "Error message"}
                },
            },
        },
    },
}

swagger_login_spec = {
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "username": {"type": "string", "description": "User's username"},
                    "password": {"type": "string", "description": "User's password"},
                },
            },
        }
    ],
    "responses": {
        200: {
            "description": "Successful login",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "Login successful message",
                    },
                    "token": {
                        "type": "string",
                        "description": "Authorization token to access routes",
                    },
                },
            },
        },
        401: {
            "description": "Unauthorized. Invalid username or password",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "Error message"}
                },
            },
        },
    },
}
swagger_logout_spec = {
    "parameters": [
        {
            "name": "Authorization",
            "in": "header",
            "type": "string",
            "required": True,
            "description": "Authorization token to access routes",
        }
    ],
    "responses": {
        200: {
            "description": "Successfully logged out",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "Logout success message",
                    }
                },
            },
        },
        500: {
            "description": "Error logging out",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "Error message"}
                },
            },
        },
        401: {
            "description": "Unauthorized. User needs to log in again.",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "Error message"}
                },
            },
        },
    },
}
swagger_profile_spec = {
    "parameters": [
        {
            "name": "Authorization",
            "in": "header",
            "type": "string",
            "required": True,
            "description": "Authorization token to access routes",
        }
    ],
    "responses": {
        200: {
            "description": "Successfully fetched profile data",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "Success message"},
                    "profile_details": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string", "description": "Student name"},
                            "dob": {"type": "string", "description": "Date of Birth"},
                            "admission_no": {
                                "type": "string",
                                "description": "Admission number",
                            },
                            "university_roll_no": {
                                "type": "string",
                                "description": "University Roll number",
                            },
                        },
                    },
                },
            },
        },
        401: {
            "description": "Unauthorized. Authorization token expired. Please login again.",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "Error message"}
                },
            },
        },
    },
}

swagger_status_spec = {
    "responses": {
        200: {
            "description": "Successfully retrieved status",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "Status message"}
                },
            },
        },
    },
}

swagger_present_spec = {
    "parameters": [
        {
            "name": "month",
            "in": "query",
            "type": "integer",
            "required": True,
            "description": "Month (1-12)",
        },
        {
            "name": "semester",
            "in": "query",
            "type": "integer",
            "required": True,
            "description": "Semester (1-8)",
        },
        {
            "name": "year",
            "in": "query",
            "type": "integer",
            "required": True,
            "description": "Year",
        },
        {
            "name": "Authorization",
            "in": "header",
            "type": "string",
            "required": True,
            "description": "Authorization token to access routes",
        },
    ],
    "responses": {
        200: {
            "description": "Successfully fetched data",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "Success message"},
                    "data": {
                        "type": "object",
                        "properties": {
                            "month": {"type": "string", "description": "Month"},
                            "month_num": {
                                "type": "string",
                                "description": "Month number",
                            },
                            "semester": {"type": "string", "description": "Semester"},
                            "semester_num": {
                                "type": "string",
                                "description": "Semester number",
                            },
                            "year": {"type": "string", "description": "Year"},
                            "present_hours": {
                                "type": "array",
                                "description": "List of present hours data",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "day": {
                                            "type": "integer",
                                            "description": "Day of the month",
                                        },
                                        "hour": {
                                            "type": "integer",
                                            "description": "Hour",
                                        },
                                        "subject_code": {
                                            "type": "string",
                                            "description": "Subject code",
                                        },
                                        "subject_name": {
                                            "type": "string",
                                            "description": "Subject name",
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        400: {
            "description": "Invalid parameters",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "Error message"}
                },
            },
        },
        401: {
            "description": "Authorization token expired. Please login again.",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "Error message"}
                },
            },
        },
        500: {
            "description": "Failed to fetch or parse data",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "Error message"}
                },
            },
        },
    },
}

swagger_timetable_spec = {
    "parameters": [
        {
            "name": "Authorization",
            "in": "header",
            "type": "string",
            "required": True,
            "description": "Authorization token to access routes",
        }
    ],
    "responses": {
        200: {
            "description": "Successfully retrieved timetable",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "Success message"},
                    "timetable": {
                        "type": "object",
                        "description": "Timetable data for each day and period",
                        "properties": {
                            "monday": {
                                "type": "object",
                                "description": "Timetable for Monday",
                            },
                            "tuesday": {
                                "type": "object",
                                "description": "Timetable for Tuesday",
                            },
                            "wednesday": {
                                "type": "object",
                                "description": "Timetable for Wednesday",
                            },
                            "thursday": {
                                "type": "object",
                                "description": "Timetable for Thursday",
                            },
                            "friday": {
                                "type": "object",
                                "description": "Timetable for Friday",
                            },
                        },
                    },
                },
            },
        },
        404: {
            "description": "Timetable data not found",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "Error message"}
                },
            },
        },
        401: {
            "description": "Unauthorized. Authorization token expired. Please login again.",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "Error message"}
                },
            },
        },
    },
}

swagger_config = {
    "headers": [
        ("Access-Control-Allow-Origin", "*"),
        ("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS"),
        (
            "Access-Control-Allow-Headers",
            "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With",
        ),
    ],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json",
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/",
    "title": "RIT ETLAB portal API",
    "version": "1.0",
    "description": "Unoffical API for RIT ETLAB portal",
}

swagger_absent_spec = {
    "parameters": [
        {
            "name": "month",
            "in": "query",
            "type": "integer",
            "required": True,
            "description": "Month (1-12)",
        },
        {
            "name": "semester",
            "in": "query",
            "type": "integer",
            "required": True,
            "description": "Semester (1-8)",
        },
        {
            "name": "year",
            "in": "query",
            "type": "integer",
            "required": True,
            "description": "Year",
        },
        {
            "name": "Authorization",
            "in": "header",
            "type": "string",
            "required": True,
            "description": "Authorization token to access routes",
        },
    ],
    "responses": {
        200: {
            "description": "Successfully fetched data",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "Success message"},
                    "data": {
                        "type": "object",
                        "properties": {
                            "month": {"type": "string", "description": "Month"},
                            "month_num": {
                                "type": "string",
                                "description": "Month number",
                            },
                            "semester": {"type": "string", "description": "Semester"},
                            "semester_num": {
                                "type": "string",
                                "description": "Semester number",
                            },
                            "year": {"type": "string", "description": "Year"},
                            "absent_hours": {
                                "type": "array",
                                "description": "List of absent hours data",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "day": {
                                            "type": "integer",
                                            "description": "Day of the month",
                                        },
                                        "hour": {
                                            "type": "integer",
                                            "description": "Hour",
                                        },
                                        "subject_code": {
                                            "type": "string",
                                            "description": "Subject code",
                                        },
                                        "subject_name": {
                                            "type": "string",
                                            "description": "Subject name",
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        400: {
            "description": "Invalid parameters",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "Error message"}
                },
            },
        },
        401: {
            "description": "Authorization token expired. Please login again.",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "Error message"}
                },
            },
        },
        500: {
            "description": "Failed to fetch or parse data",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "Error message"}
                },
            },
        },
    },
}
