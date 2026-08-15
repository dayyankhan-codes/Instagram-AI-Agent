from agents.image_analyzer import analyze_image


def analyze_carousel(uploaded_files, progress_callback=None):

    results = []

    total_images = len(uploaded_files)

    for index, file in enumerate(uploaded_files):

        current_image = index + 1

        print(
            f"Analyzing image "
            f"{current_image} of {total_images}: "
            f"{file.name}"
        )

        analysis = analyze_image(file)

        results.append(
            {
                "image_number": current_image,
                "filename": file.name,
                "analysis": analysis
            }
        )

        if progress_callback:

            progress = current_image / total_images

            progress_callback(
                progress,
                current_image,
                total_images,
                file.name
            )

    return results