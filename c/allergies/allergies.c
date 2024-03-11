#include "allergies.h"

// int main()
// {
//     get_allergens(257);
// }

bool is_allergic_to(allergen_t allergen, int score)
{
    int initial_score = 128;
    int allergy_enum = 7;

    // Ignore allergies above 256
    while (score > 256)
    {
        score -= 256;
    }

    while (score > 0)
    {
        if (score - initial_score >= 0 && allergy_enum >= 0)
        {
            score -= initial_score;
            if (allergy_enum == (int)allergen)
            {
                return true;
            }
        }
        initial_score /= 2;
        allergy_enum -= 1;
    }
    return false;
}

allergen_list_t get_allergens(int score)
{
    allergen_list_t allergen_list;
    allergen_list.count = 0;
    for (int i = 0; i < ALLERGEN_COUNT; i++)
    {
        if (is_allergic_to((allergen_t)i, score))
        {
            allergen_list.allergens[i] = true;
            allergen_list.count++;
        }
        else
        {
            allergen_list.allergens[i] = false;
        }
    }
    return allergen_list;
}
