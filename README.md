# Django with Graphql Task 

## Without GraphQL (used default mechanism for CRUD operations)
1. ✔️ Create 3 tables named order, product, product_images
2. ✔️ order table is associated with product table in 1 to many relationship
3. ✔️ product table is associated with product_images in 1 to many relationship
3. ✔️ create a form and render a view to submit product attributes (name,price,quantity, images)
4. ✖️ on submit form validate form and show errors on html view

## With GraphQL
1. ✔️ create type classes of above tables
2. ✔️ create mutation classes to create, update and delete above table data.
3. ✔️ after creating mutation classes, test it on graphql-playground
4. ✔️ graphql-playground should have following queries:
  - ✔️ product(get single product by id)
  - ✔️ products(multiple products)
  - ✖️ uploadImage(upload an image to product images and associate it with product table)
  - ✔️ deleteImage(delete image)
  - ✔️ order(get order by id)
  - ✔️ orders(get all saved orders)


## Tech Stack
- Django
- Graphql
