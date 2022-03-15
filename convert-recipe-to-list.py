recipe = '''½ (12 ounce) can CONTADINA® Tomato Paste

1 teaspoon dried oregano, crushed

1 teaspoon dried basil, crushed

½ teaspoon garlic powder

½ teaspoon onion powder

½ teaspoon sugar

½ teaspoon salt

¼ teaspoon black pepper

3 ¼ cups all-purpose flour, or more as needed

2 (.25 ounce) envelopes FLEISCHMANN'S® Pizza Crust Yeast or RapidRise® Yeast

1 tablespoon sugar

1 ½ teaspoons salt

1 ⅓ cups very warm water (120 degrees F to 130 degrees F)

⅓ cup oil

1 (6 ounce) package HORMEL® Pepperoni

1 cup shredded mozzarella cheese, or more to taste'''

res = recipe.split(sep="\n\n")
# print(res)

for a in res:
    # print(a)
    print("<li>" + a + "</li>")
