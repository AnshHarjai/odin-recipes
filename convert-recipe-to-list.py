recipe = '''12 uncooked lasagna noodles
1 pound sweet Italian sausage
⅔ cup chopped onions
½ tablespoon minced garlic
⅔ cup chopped fresh parsley, divided
3 (6 ounce) cans tomato paste
1 (15 ounce) can tomato sauce
2 cups water
1 ½ teaspoons Italian seasoning
1 ½ teaspoons dried oregano
1 ½ teaspoons dried basil leaves
1 pound part-skim ricotta cheese
1 (10 ounce) package chopped spinach, thawed and squeeze dried
½ cup grated Parmesan cheese
3 eggs
2 teaspoons garlic salt
¼ teaspoon ground black pepper
3 cups shredded mozzarella cheese'''

res = recipe.split(sep="\n")
# print(res)
for a in res:
    print("<li>" + a + "</li>")
