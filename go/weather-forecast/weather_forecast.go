// Package weather forecasts the weather.
package weather

// CurrentCondition represents the current weather condition.
var CurrentCondition string

// CurrentLocation represents the current weather location.
var CurrentLocation string

// Forecast returns the weather forecast for the given city and condition.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
