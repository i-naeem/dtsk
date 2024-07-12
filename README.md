# Django with Graphql Task

## Without GraphQL (used default mechanism for CRUD operations)

1. ✔️ Create 3 tables named order, product, product_images
2. ✔️ order table is associated with product table in 1 to many relationship
3. ✔️ product table is associated with product_images in 1 to many relationship
4. ✔️ create a form and render a view to submit product attributes (name,price,quantity, images)
5. ✔️ on submit form validate form and show errors on html view

## With GraphQL

1. ✔️ create type classes of above tables
2. ✔️ create mutation classes to create, update and delete above table data.
3. ✔️ after creating mutation classes, test it on graphql-playground
4. ✔️ graphql-playground should have following queries:
    - ✔️ product(get single product by id)
    - ✔️ products(multiple products)
    - ✖️ uploadImage(upload an image to product images and associate it with product table) <br/>
      > I tried `graphene_file_upload` and everything but I could not find a way to upload image from `graphiql` interface,I can pass the url and associate that with the product but I was unable to find a way to upload an image from the `graphiql` interface so I created `create_image` view that have the form to upload images and associate those images with product.

    - ✔️ deleteImage(delete image)
    - ✔️ order(get order by id)
    - ✔️ orders(get all saved orders)

## Tech Stack

- Django
- Graphql
