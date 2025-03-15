from flask import Flask, render_template, request
from api_fetcher import fetch_weather
from data_scraper import scrape_news
from data_analysis import plot_data

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    error_messages = []
    city = "New York"
    temp = None
    city_name = None
    news = []
    plot_path = None

    if request.method == "POST":
        city = request.form.get("city", "").strip()
        if not city:
            error_messages.append("Please enter a valid city name.")
        else:
            try:
                temp, city_name = fetch_weather(city)
            except Exception as e:
                error_messages.append(f"Weather fetch error: {str(e)}")

    # Fetch latest news
    try:
        news = scrape_news()
    except Exception as e:
        error_messages.append(f"News fetch error: {str(e)}")

    # Generate data visualization
    try:
        plot_path = plot_data()
    except Exception as e:
        error_messages.append(f"Plot generation error: {str(e)}")

    return render_template(
        "index.html",
        temp=temp,
        city=city_name if city_name else city,
        news=news,
        plot_path=plot_path,
        error=" | ".join(error_messages) if error_messages else None
    )


if __name__ == "__main__":
    app.run(debug=True)
