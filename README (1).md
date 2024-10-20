## What it Does

**Harmony Health** is an AI-powered platform that provides users with personalized wellness strategies by analyzing their emotions. The application tracks users' emotional states using advanced AI technologies, such as voice and facial recognition. By integrating with the Hume API, it allows users to gain insights into their mental health over time, identifying patterns of emotional distress and helping users take proactive steps towards better mental well-being.

## Watch Harmony Health in Action

Here is a demonstration of Harmony Health:

[![Harmony Health Demo](https://img.youtube.com/vi/qy-2ni6_WFo/0.jpg)](https://www.youtube.com/watch?v=qy-2ni6_WFo)

Click on the image above to watch the video demo on YouTube.

## How We Built It

Harmony Health was built using the following technologies and tools:

- **Python** as the primary programming language.
- **Hume API** for emotion tracking through voice and facial recognition.
- **Flask** for developing the backend.
- **TensorFlow** for AI and machine learning-based emotion analysis.
- **Google Cloud** for hosting and data processing.
- **Twilio** for sending notifications based on emotional insights.

## Challenges We Ran Into

One of the challenges we faced was integrating real-time emotion detection using both facial expressions and vocal tones. Another issue was the complexity of analyzing multiple data points over time, while ensuring the system's feedback remained accurate and relevant. Additionally, handling large-scale data efficiently and securely required fine-tuning our cloud infrastructure.

## Accomplishments We're Proud Of

We are proud of creating a comprehensive platform that can track and analyze emotions with a high degree of accuracy. The integration of the Hume API, along with our custom machine learning models, allowed us to offer personalized wellness recommendations that users can benefit from. Furthermore, we managed to make the app both responsive and intuitive, which makes it easier for users to take control of their mental well-being.

## What We Learned

Throughout the project, we learned a great deal about:

- The technical aspects of **emotion detection** using AI.
- Advanced integrations with APIs like **Hume** for emotion tracking.
- Handling large-scale data with **Google Cloud**.
- Building user-friendly interfaces using **Flask**.
- The challenges of designing mental health platforms, including ethical considerations and user privacy.

## What's Next for Harmony Health

The future of **Harmony Health** involves:

- Expanding the application to include more comprehensive mental health assessments.
- Integrating wearable devices to enhance the real-time tracking of physical and emotional health data.
- Developing native mobile applications for **iOS** and **Android** to expand accessibility.
- Offering users long-term wellness strategies through personalized mental health insights and action plans.

## Hackathon Experience

**Harmony Health** was built during a 36-hour hackathon called the **UC Berkeley AI Hackathon 2024**. Despite the short timeframe, we were able to complete a fully functional prototype that delivers real value. You can learn more about the hackathon at [UC Berkeley AI Hackathon 2024](https://uc-berkeley-ai-hackathon-2024.devpost.com/).


## Use the Project Yourself!

Follow these instructions to set up the project on your local machine for development and testing purposes. For deployment notes on live systems, see the section below.

### Prerequisites

You'll need the following software installed before running the project:

- Python 3.x
- Flask (`pip install flask`)
- Hume API setup
- TensorFlow (`pip install tensorflow`)
- Twilio (`pip install twilio`)
- Google Cloud setup

pip install flask tensorflow twilio


### Installing

Follow this step-by-step guide to set up a development environment:

1. **Clone the repository:**

git clone https://github.com/1300Sarthak/HarmonyHealth


2. **Navigate to the project directory:**

cd HarmonyHealth


3. **Install the required dependencies:**

pip install -r requirements.txt


4. **Run the application locally:**

python app.py


5. **Test the emotion tracking:**  
The application will start analyzing user emotions based on their voice and facial expressions, providing personalized mental health insights.

Repeat steps 1-4 until fully set up.

## Running the Tests

To run automated tests for the system, use the following commands.

### Break Down into End-to-End Tests

These tests validate the integration of all modules, ensuring that emotion tracking works correctly end-to-end. This includes testing facial expression and vocal tone detection.

python test_end_to_end.py


### Coding Style Tests

Ensure that the code adheres to PEP8 coding standards. This improves readability and maintainability.

flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics


## Deployment

To deploy **Harmony Health** on a live system, follow these steps:

    1. Deploy the Flask web app using a platform like **Heroku** or **AWS**.
    2. Ensure that all necessary API integrations (Hume API, Google Cloud) are properly configured.
    3. Add environment variables for API keys where applicable.

## Built With

* **Hume API** - For emotion tracking
* **OpenCV** - Library for video capture and processing
* **TensorFlow** - AI and ML functionality
* **Flask** - Web framework
* **Google Cloud** - For hosting and data storage
* **Twilio** - For notifications

## Authors

- **Sarthak Sethi** - [GitHub](https://github.com/SarthakSethi)
- **Shivam Singh** 
- **Sharva Santakumar** - [GitHub](https://github.com/sharvuncle)
- **Holland Pleskac** - [GitHub](https://github.com/HollandPleskac)

## Acknowledgments

- Thanks to the **UC Berkeley AI Hackathon 2024** organizers for hosting the event and providing a platform to bring this project to life.
- Appreciation to the open-source community for developing tools like **TensorFlow**, and **Hume API**, which made the development of Harmony Health possible.
- Inspiration drawn from mental health platforms like **Headspace** and **Calm**, which guided the focus on providing users with meaningful mental wellness insights.


