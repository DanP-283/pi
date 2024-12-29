import tkinter as tk
from tkinter import ttk
import requests
import random
import json
from datetime import datetime
import webbrowser
from PIL import Image, ImageTk
import io
import threading
import time
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import sys
import os

# API Keys
WEATHER_API_KEY = "a94fc2e53d894c76b4f215341242312"
NEWS_API_KEY = "27bfa13de41c4ff8b0ad9fb10b3e6458"

# Default URL for the browser
DEFAULT_URL = "https://www.google.com"

# Disney facts
DISNEY_FACTS = [
    "Mickey Mouse's original name was Mortimer Mouse",
    "Walt Disney holds the record for most Academy Awards",
    "Disneyland opened in 1955",
    "Snow White and the Seven Dwarfs was Disney's first full-length animated film",
    "Walt Disney was afraid of mice",
    "The original voice of Mickey Mouse was Walt Disney himself",
    "Dumbo is the shortest of the Disney animated features at 64 minutes",
    "Disney World is the size of San Francisco",
    "There are hidden Mickeys throughout Disney parks",
    "The Pirates of the Caribbean ride was built in 1967",
    "Cinderella Castle is made of fiberglass",
    "Disney World has an underground tunnel system",
    "The first Disney character to speak was Minnie Mouse",
    "Donald Duck's middle name is Fauntleroy",
    "The Lion King was originally called 'King of the Jungle'",
    "Tinker Bell's design was based on Marilyn Monroe",
    "Sleeping Beauty Castle was inspired by Neuschwanstein Castle in Germany",
    "Walt Disney never graduated from high school",
    "Disney World has its own government district",
    "The first Mickey Mouse color cartoon was 'The Band Concert' in 1935",
    "Disneyland's opening day was a disaster",
    "There are no mosquitoes in Disney World due to careful planning",
    "Walt Disney was dyslexic",
    "The Haunted Mansion's pet cemetery was added in the 1990s",
    "Epcot was originally planned as a real city",
    "Mickey Mouse has 4 fingers to save animation time",
    "The first Disney princess was Snow White",
    "Buzz Lightyear was originally named Lunar Larry",
    "The Magic Kingdom's castle is actually pink, not white",
    "Walt Disney's first company went bankrupt",
    "The original Disneyland ticket prices were $1 for adults",
    "Aladdin's Genie wears a Hawaiian shirt in one scene",
    "101 Dalmatians was the first film to use xerography",
    "The Tree of Life at Animal Kingdom has over 300 carvings",
    "Mary Poppins was Walt Disney's favorite film",
    "Disneyland's Main Street USA is based on Walt's hometown",
    "The first Disney Store opened in 1987",
    "Beauty and the Beast was the first animated film nominated for Best Picture",
    "Walt Disney created Mickey Mouse on a train ride",
    "The Disney family crest is featured in It's a Small World",
    "Cinderella's Castle contains a secret suite",
    "Disney's Nine Old Men were the core animators",
    "The first Disney theme park outside the US was Tokyo Disneyland",
    "Walt Disney won 32 Academy Awards",
    "The original Space Mountain opened in 1975",
    "Disney World has over 62,000 employees",
    "Tinker Bell performs the last flight over Disneyland at night",
    "The Matterhorn was the first tubular steel track roller coaster",
    "Disney's first cartoon character was Oswald the Lucky Rabbit",
    "The Disney cruise line has its own private island",
    "Walt Disney's first job was as a newspaper artist",
    "The Haunted Mansion's singing busts are called the Mellomen",
    "Disney World uses enough fabric for costumes to cover Manhattan",
    "The original Peter Pan's Flight had guests flying as Peter",
    "Club 33 is Disneyland's secret members-only club",
    "The first Disney film to use CGI was The Black Cauldron",
    "Walt Disney's favorite character was Goofy",
    "The Jungle Cruise's water is dyed brown to hide the track",
    "Disney World has over 30,000 hotel rooms",
    "The first Disney character to receive a star on Hollywood Walk of Fame was Mickey Mouse",
    "The Twilight Zone Tower of Terror drops guests at 39 mph",
    "Walt Disney was a train enthusiast",
    "The Pirates of the Caribbean ride inspired the movie series",
    "Disney's California Adventure opened in 2001",
    "The first Disney animated feature in 3D was Chicken Little",
    "Walt Disney's office is preserved exactly as he left it",
    "The Disney Archives were established in 1970",
    "Disneyland's Haunted Mansion has 999 happy haunts",
    "The first Disney theme park in Europe was Disneyland Paris",
    "Mickey Mouse's first words were 'Hot dogs!'",
    "Walt Disney had a private apartment above the Fire Station",
    "The Disney Vault was a real marketing strategy",
    "Finding Nemo Submarine Voyage replaced the original submarine ride",
    "Disney's Animal Kingdom opened in 1998",
    "The first Disney character merchandise was a Mickey Mouse tablet",
    "Walt Disney's first animation studio was in his garage",
    "Disney World's castle is taller than Disneyland's",
    "The first Disney TV show aired in 1954",
    "Pirates of the Caribbean was the last ride Walt Disney worked on",
    "Disney's Hollywood Studios opened as Disney-MGM Studios",
    "The first Disney comic strip appeared in 1930",
    "Walt Disney was a high school dropout",
    "The Disney Company was founded in 1923",
    "Disneyland's opening day was invitation-only",
    "The first Disney character to wear gloves was Mickey Mouse",
    "Walt Disney's first cartoon company went bankrupt",
    "The first Disney theme park in China was Hong Kong Disneyland",
    "Mickey Mouse's first appearance was in Plane Crazy",
    "Disney World opened on October 1, 1971",
    "The first Disney live-action film was Treasure Island",
    "Walt Disney's first successful cartoon series was Alice Comedies",
    "Disney's first full-length feature took three years to make",
    "The first Disney character merchandise was a Mickey Mouse watch",
    "Walt Disney's first job was as a newspaper delivery boy",
    "The first Disney character to speak was Mickey Mouse",
    "Disney's first television series was Disneyland",
    "The first Disney theme park in Europe opened in 1992",
    "Walt Disney's first animated feature cost $1.4 million",
    "The first Disney character to have a star on Hollywood Walk of Fame was Mickey Mouse",
    "Disney's first color cartoon was Flowers and Trees",
    "Walt Disney's first studio was called Laugh-O-Gram",
    "The first Disney character to have a comic book was Mickey Mouse",
    "Disney's first Academy Award was for Flowers and Trees",
    "The first Disney character to have a balloon in Macy's Parade was Mickey Mouse",
    "Walt Disney's first cartoon series was Newman Laugh-O-Grams",
    "The first Disney character to have a radio show was Mickey Mouse",
    "Disney's first feature-length film cost $1.5 million",
    "The first Disney character to have a comic strip was Mickey Mouse",
    "Walt Disney's first cartoon company was called Iwerks-Disney Commercial Artists",
    "The first Disney character to have a theme park was Mickey Mouse",
    "Disney's first animated feature took over 750 artists",
    "The first Disney character to have a video game was Mickey Mouse",
    "Walt Disney's first animated short was Alice's Wonderland",
    "The first Disney character to have a plush toy was Mickey Mouse",
    "Disney's first animated feature used over 2 million drawings",
    "The first Disney character to have a birthday party was Mickey Mouse",
    "Walt Disney's first animation job was at Pesmen-Rubin Art Studio",
    "The first Disney character to have a fan club was Mickey Mouse",
    "Disney's first animated feature used 1,500 shades of paint",
    "The first Disney character to have a newspaper comic was Mickey Mouse",
    "Walt Disney's first animation company was called Laugh-O-Gram Films",
    "The first Disney character to have a magazine was Mickey Mouse",
    "Disney's first animated feature had over 250,000 cels",
    "The first Disney character to have a record album was Mickey Mouse",
    "Walt Disney's first film studio was in Kansas City",
    "The first Disney character to have a book series was Mickey Mouse",
    "Disney's first animated feature took over 3 years to complete",
    "The first Disney character to have a television show was Mickey Mouse",
    "Walt Disney's first cartoon series was Oswald the Lucky Rabbit",
    "The first Disney character to have a parade was Mickey Mouse",
    "Disney's first animated feature premiered at the Carthay Circle Theatre",
    "The first Disney character to have a theme song was Mickey Mouse",
    "Walt Disney's first successful cartoon was Alice Comedies",
    "The first Disney character to have a birthday celebration was Mickey Mouse",
    "Disney's first animated feature was released in 1937",
    "The first Disney character to have a merchandise line was Mickey Mouse",
    "Walt Disney's first cartoon company was in Kansas City",
    "The first Disney character to have a fan magazine was Mickey Mouse",
    "Disney's first animated feature was Snow White and the Seven Dwarfs",
    "The first Disney character to have a stage show was Mickey Mouse",
    "Walt Disney's first animation studio was in his uncle's garage",
    "The first Disney character to have a theme park attraction was Mickey Mouse",
    "Disney's first animated feature was dubbed in multiple languages",
    "The first Disney character to have a Christmas special was Mickey Mouse",
    "Walt Disney's first cartoon series was called Newman Laugh-O-Grams",
    "The first Disney character to have a Halloween special was Mickey Mouse",
    "Disney's first animated feature was released during the Great Depression",
    "The first Disney character to have a birthday cake was Mickey Mouse",
    "Walt Disney's first animation company was in Los Angeles",
    "The first Disney character to have a Valentine's Day special was Mickey Mouse",
    "Disney's first animated feature was released in multiple countries",
    "The first Disney character to have an Easter special was Mickey Mouse",
    "Walt Disney's first successful business was the Disney Brothers Studio",
    "The first Disney character to have a Thanksgiving special was Mickey Mouse",
    "Disney's first animated feature was released worldwide",
    "The first Disney character to have a New Year's special was Mickey Mouse",
    "Walt Disney's first successful cartoon was Steamboat Willie",
    "The first Disney character to have a Fourth of July special was Mickey Mouse",
    "Disney's first animated feature was a box office success",
    "The first Disney character to have a St. Patrick's Day special was Mickey Mouse",
    "Walt Disney's first cartoon company was called Disney Brothers Cartoon Studio",
    "The first Disney character to have a Mother's Day special was Mickey Mouse",
    "Disney's first animated feature was a critical success",
    "The first Disney character to have a Father's Day special was Mickey Mouse",
    "Walt Disney's first successful cartoon series was Mickey Mouse",
    "The first Disney character to have a Labor Day special was Mickey Mouse",
    "Disney's first animated feature was a technological breakthrough",
    "The first Disney character to have a Memorial Day special was Mickey Mouse",
    "Walt Disney's first successful business venture was animation",
    "The first Disney character to have a Columbus Day special was Mickey Mouse",
    "Disney's first animated feature was a financial success",
    "The first Disney character to have a Veterans Day special was Mickey Mouse",
    "Walt Disney's first successful cartoon character was Mickey Mouse",
    "The first Disney character to have a Presidents' Day special was Mickey Mouse",
    "Disney's first animated feature was an artistic triumph",
    "The first Disney character to have a Groundhog Day special was Mickey Mouse",
    "Walt Disney's first successful movie was Snow White",
    "The first Disney character to have a Flag Day special was Mickey Mouse",
    "Disney's first animated feature was a commercial success",
    "The first Disney character to have an April Fools' Day special was Mickey Mouse",
    "Walt Disney's first successful theme park was Disneyland",
    "The first Disney character to have a May Day special was Mickey Mouse",
    "Disney's first animated feature was an industry milestone",
    "The first Disney character to have an Earth Day special was Mickey Mouse",
    "Walt Disney's first successful TV show was Disneyland",
    "The first Disney character to have an Arbor Day special was Mickey Mouse",
    "Disney's first animated feature was a cultural phenomenon",
    "The first Disney character to have a World Peace Day special was Mickey Mouse"
]

class BrowserWidget(QWidget):
    def __init__(self, url=DEFAULT_URL):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(url))
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Raspberry Pi Dashboard")
        self.root.attributes('-fullscreen', True)
        
        # Initialize PyQt application
        self.qt_app = QApplication.instance()
        if not self.qt_app:
            self.qt_app = QApplication(sys.argv)
        
        # Create main container
        self.main_container = ttk.Frame(self.root)
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Create left and right panes
        self.setup_left_pane()
        self.right_pane = ttk.Frame(self.main_container, width=400)
        self.right_pane.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False)
        
        # Create right pane sections
        self.weather_frame = ttk.LabelFrame(self.right_pane, text="Weather")
        self.disney_frame = ttk.LabelFrame(self.right_pane, text="Disney Fact of the Day")
        self.news_frame = ttk.LabelFrame(self.right_pane, text="US News Ticker")
        
        self.weather_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.disney_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.news_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Initialize components
        self.setup_weather()
        self.setup_disney_fact()
        self.setup_news_ticker()
        
        # Start update threads
        self.start_update_threads()
        
        # Setup periodic PyQt updates
        self.root.after(100, self.process_qt_events)

    def setup_left_pane(self):
        # Create a frame for the browser
        self.left_pane = ttk.Frame(self.main_container)
        self.left_pane.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Create and embed the browser widget
        self.browser_widget = BrowserWidget()
        self.browser_container = tk.Frame(self.left_pane)
        self.browser_container.pack(fill=tk.BOTH, expand=True)
        
        # Embed the PyQt widget into tkinter
        self.browser_widget.browser.setParent(None)
        self.browser_widget.browser.setAttribute(Qt.WA_DontCreateNativeAncestors)
        self.browser_widget.browser.setAttribute(Qt.WA_NativeWindow)
        self.browser_widget.browser.setWindowFlags(Qt.FramelessWindowHint)
        
        # Get the window ID of the tkinter container
        self.browser_container.update()
        container_id = self.browser_container.winfo_id()
        
        # Embed the browser
        self.browser_widget.browser.windowHandle().setParent(container_id)
        
        # Configure size
        self.browser_container.bind("<Configure>", self.on_browser_resize)

    def on_browser_resize(self, event):
        if hasattr(self, 'browser_widget'):
            self.browser_widget.browser.setFixedSize(event.width, event.height)

    def process_qt_events(self):
        self.qt_app.processEvents()
        self.root.after(100, self.process_qt_events)

    def navigate_to_url(self, url):
        self.browser_widget.browser.setUrl(QUrl(url))

    def setup_weather(self):
        self.weather_label = ttk.Label(self.weather_frame, text="Loading weather...")
        self.weather_label.pack(padx=10, pady=10)
        self.update_weather()
        
    def setup_disney_fact(self):
        self.fact_label = ttk.Label(self.disney_frame, text="Loading fact...", wraplength=380)
        self.fact_label.pack(padx=10, pady=10)
        self.update_disney_fact()
        
    def setup_news_ticker(self):
        self.news_label = ttk.Label(self.news_frame, text="Loading news...", wraplength=380)
        self.news_label.pack(padx=10, pady=10)
        self.current_news_index = 0
        self.news_headlines = []
        self.update_news()
        
    def update_weather(self):
        try:
            url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q=28376"
            response = requests.get(url)
            data = response.json()
            
            current = data['current']
            temp_f = current['temp_f']
            condition = current['condition']['text']
            
            weather_text = f"Temperature: {temp_f}°F\nCondition: {condition}"
            self.weather_label.config(text=weather_text)
        except Exception as e:
            self.weather_label.config(text=f"Weather Error: {str(e)}")
        
        # Update every 30 minutes
        self.root.after(1800000, self.update_weather)
        
    def update_disney_fact(self):
        fact = random.choice(DISNEY_FACTS)
        self.fact_label.config(text=fact)
        # Update daily
        self.root.after(86400000, self.update_disney_fact)
        
    def update_news(self):
        try:
            url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
            response = requests.get(url)
            data = response.json()
            
            self.news_headlines = [article['title'] for article in data['articles']]
            self.rotate_news()
        except Exception as e:
            self.news_label.config(text=f"News Error: {str(e)}")
        
        # Update news list every hour
        self.root.after(3600000, self.update_news)
        
    def rotate_news(self):
        if self.news_headlines:
            self.current_news_index = (self.current_news_index + 1) % len(self.news_headlines)
            self.news_label.config(text=self.news_headlines[self.current_news_index])
        
        # Rotate headlines every 10 seconds
        self.root.after(10000, self.rotate_news)
        
    def start_update_threads(self):
        # Start initial updates
        self.update_weather()
        self.update_disney_fact()
        self.update_news()

def main():
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
