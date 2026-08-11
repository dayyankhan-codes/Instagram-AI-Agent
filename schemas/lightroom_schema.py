LIGHTROOM_SCHEMA = {
    "type": "object",
    "properties": {
        "basic": {
            "type": "object",
            "properties": {
                "Exposure": {"type": "string"},
                "Contrast": {"type": "string"},
                "Highlights": {"type": "string"},
                "Shadows": {"type": "string"},
                "Whites": {"type": "string"},
                "Blacks": {"type": "string"},
            },
            "required": [
                "Exposure",
                "Contrast",
                "Highlights",
                "Shadows",
                "Whites",
                "Blacks",
            ],
        },

        "basic_why": {"type": "string"},

        "white_balance": {
            "type": "object",
            "properties": {
                "Temperature": {"type": "string"},
                "Tint": {"type": "string"},
            },
            "required": ["Temperature", "Tint"],
        },

        "white_balance_why": {"type": "string"},

        "presence": {
            "type": "object",
            "properties": {
                "Texture": {"type": "string"},
                "Clarity": {"type": "string"},
                "Dehaze": {"type": "string"},
                "Vibrance": {"type": "string"},
                "Saturation": {"type": "string"},
            },
            "required": [
                "Texture",
                "Clarity",
                "Dehaze",
                "Vibrance",
                "Saturation",
            ],
        },

        "presence_why": {"type": "string"},

        "tone_curve": {
            "type": "object",
            "properties": {
                "Lights": {"type": "string"},
                "Darks": {"type": "string"},
                "Highlights": {"type": "string"},
                "Shadows": {"type": "string"},
            },
            "required": [
                "Lights",
                "Darks",
                "Highlights",
                "Shadows",
            ],
        },

        "tone_curve_why": {"type": "string"},

        "hsl": {
            "type": "object",
            "properties": {
                "Red": {
                    "type": "object",
                    "properties": {
                        "Hue": {"type": "string"},
                        "Saturation": {"type": "string"},
                        "Luminance": {"type": "string"},
                    },
                },
                "Orange": {
                    "type": "object",
                    "properties": {
                        "Hue": {"type": "string"},
                        "Saturation": {"type": "string"},
                        "Luminance": {"type": "string"},
                    },
                },
                "Yellow": {
                    "type": "object",
                    "properties": {
                        "Hue": {"type": "string"},
                        "Saturation": {"type": "string"},
                        "Luminance": {"type": "string"},
                    },
                },
                "Green": {
                    "type": "object",
                    "properties": {
                        "Hue": {"type": "string"},
                        "Saturation": {"type": "string"},
                        "Luminance": {"type": "string"},
                    },
                },
                "Aqua": {
                    "type": "object",
                    "properties": {
                        "Hue": {"type": "string"},
                        "Saturation": {"type": "string"},
                        "Luminance": {"type": "string"},
                    },
                },
                "Blue": {
                    "type": "object",
                    "properties": {
                        "Hue": {"type": "string"},
                        "Saturation": {"type": "string"},
                        "Luminance": {"type": "string"},
                    },
                },
                "Purple": {
                    "type": "object",
                    "properties": {
                        "Hue": {"type": "string"},
                        "Saturation": {"type": "string"},
                        "Luminance": {"type": "string"},
                    },
                },
                "Magenta": {
                    "type": "object",
                    "properties": {
                        "Hue": {"type": "string"},
                        "Saturation": {"type": "string"},
                        "Luminance": {"type": "string"},
                    },
                },
            },
        },

        "hsl_why": {"type": "string"},

        "color_grading": {
            "type": "object",
            "properties": {
                "Shadows": {
                    "type": "object",
                    "properties": {
                        "Hue": {"type": "string"},
                        "Saturation": {"type": "string"},
                    },
                },
                "Midtones": {
                    "type": "object",
                    "properties": {
                        "Hue": {"type": "string"},
                        "Saturation": {"type": "string"},
                    },
                },
                "Highlights": {
                    "type": "object",
                    "properties": {
                        "Hue": {"type": "string"},
                        "Saturation": {"type": "string"},
                    },
                },
                "Balance": {"type": "string"},
            },
        },

        "color_grading_why": {"type": "string"},

        "detail": {
            "type": "object",
            "properties": {
                "Sharpening": {"type": "string"},
                "Radius": {"type": "string"},
                "Detail": {"type": "string"},
                "Masking": {"type": "string"},
                "Noise Reduction": {"type": "string"},
                "Color Noise Reduction": {"type": "string"},
            },
        },

        "detail_why": {"type": "string"},

        "lens_corrections": {
            "type": "object",
            "properties": {
                "Enable Profile Corrections": {"type": "string"},
                "Remove Chromatic Aberration": {"type": "string"},
            },
        },

        "lens_corrections_why": {"type": "string"},

        "effects": {
            "type": "object",
            "properties": {
                "Post Crop Vignette": {"type": "string"},
                "Grain": {"type": "string"},
            },
        },

        "effects_why": {"type": "string"},

        "calibration": {
            "type": "object",
            "properties": {
                "Red Primary Hue": {"type": "string"},
                "Red Primary Saturation": {"type": "string"},
                "Green Primary Hue": {"type": "string"},
                "Green Primary Saturation": {"type": "string"},
                "Blue Primary Hue": {"type": "string"},
                "Blue Primary Saturation": {"type": "string"},
            },
        },

        "calibration_why": {"type": "string"},

        "masking": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "mask_type": {"type": "string"},
                    "settings": {
                        "type": "object"
                    },
                    "why": {"type": "string"},
                },
                "required": [
                    "name",
                    "mask_type",
                    "settings",
                    "why",
                ],
            },
        },
    },

    "required": [
        "basic",
        "basic_why",
        "white_balance",
        "white_balance_why",
        "presence",
        "presence_why",
        "tone_curve",
        "tone_curve_why",
        "hsl",
        "hsl_why",
        "color_grading",
        "color_grading_why",
        "detail",
        "detail_why",
        "lens_corrections",
        "lens_corrections_why",
        "effects",
        "effects_why",
        "calibration",
        "calibration_why",
        "masking",
    ],
}