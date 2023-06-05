import emoji from "react-easy-emoji";

export const intro = {
  name: "WasteWise",
  title: "WasteWise",
  description:
    "Introducing WasteWise: Revolutionizing waste management with AI-powered recycling solutions. By scanning waste items and considering local recycling rules, WasteWise provides users with clear instructions on proper disposal methods. Leveraging geolocation services, the app also locates the nearest recycling points, making waste disposal convenient and efficient. Join us in reshaping waste management practices and fostering a sustainable future with WasteWise, your recycling companion!",
};

export const imageSection = {
  title: "How It Works",
  data: [
    {
      title: "Upload Your Image",
      lottieAnimationFile: "/lottie/webdev.json", 
      steps: [
        emoji("⚡ Upload an image of your waste"),
        emoji("⚡ Processing..."),
        emoji("⚡ Get directions to the nearest waste bins at your convenience!"),
      ],
    },
  ],
};

