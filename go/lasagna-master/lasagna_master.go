package lasagna

// PreparationTime calculates the preparation time of the lasagna.
func PreparationTime(layers []string, time int) int {
	if time == 0 {
		time = 2
	}
	return len(layers) * time
}

// Quantities calculates the amount of noodles and sauce required.
func Quantities(layers []string) (noodles int, sauce float64) {
	for _, layer := range layers {
		switch layer {
		case "noodles":
			noodles += 50
		case "sauce":
			sauce += 0.2
		}
	}
	return
}

// AddSecretIngredient adds a secret ingredient to the list of ingredients.
func AddSecretIngredient(friendsList []string, myList []string) {
	myList[len(myList)-1] = friendsList[len(friendsList)-1]
}

// ScaleRecipe scales the amount of noodles and sauce for a different number of servings.
func ScaleRecipe(quantities []float64, portions int) []float64 {
	scaledPortions := []float64{}
	for i := 0; i < len(quantities); i++ {
		scaledPortions = append(scaledPortions, quantities[i]*float64(portions)/2)
	}
	return scaledPortions
}
