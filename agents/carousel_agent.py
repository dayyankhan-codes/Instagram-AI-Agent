from agents.image_analyzer import analyze_image


def analyze_carousel(uploaded_files):

    results = []

    for index, file in enumerate(uploaded_files):

        print(f"Analyzing {file.name}")

        analysis = analyze_image(file)

        results.append(
            {
                "image_number": index + 1,
                "filename": file.name,
                "analysis": analysis
            }
        )

    return results