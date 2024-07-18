axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

const { createApp, ref } = Vue;
createApp({
  data() {
    return {
      search_text: '',
      weather_forecast: {},
      cities: [],
    };
  },
  methods: {
    async fetchCities() {
      if (this.search_text.length === 0) {
        this.cities = [];
        return;
      }
      try {
        const response = await axios.get('http://' + this.host +'/api/v1/cities', {
          params: {
            city: this.search_text
          }
        });
        this.cities = response.data;
      } catch (error) {
        console.error('Error fetching cities:', error);
      }
    },
    async getWeatherForecast() {
      try {
        const response = await axios.get('http://' + this.host +'/api/v1/forecast/', {
          params: {
            city: this.search_text
          }
        });
        this.weather_forecast = response.data;
        document.getElementById('weather-info').style.display = 'block';
        localStorage.setItem('last_city', this.search_text);
      } catch (error) {
        console.error('Error fetching weather forecast:', error);
      }
    },
    selectCity(city) {
      this.search_text = city;
      this.cities = [];
    },
    async load_last_city() {
      const last_city = localStorage.getItem('last_city');
      if (last_city) {
          this.search_text = last_city;
          await this.getWeatherForecast();
      }
    }
  },
  mounted() {
    this.host = window.location.host;
    this.load_last_city();
  },
  }).mount('#app');