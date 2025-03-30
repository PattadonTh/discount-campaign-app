from core.discount import (
    FixedDiscount,
    PercentageDiscount,
    CategoryPercentageDiscount,
    PointDiscount,
    SpecialDiscount,
)


def load_campaigns(campaigns_json: list[dict]):
    discount_objects = []

    for campaign in campaigns_json:
        discount_type = campaign["type"].lower()
        params = campaign["parameters"]

        if discount_type == "fixed":
            discount_objects.append(FixedDiscount(params["amount"]))

        elif discount_type == "percentage":
            discount_objects.append(PercentageDiscount(params["percentage"]))

        elif discount_type == "points":
            discount_objects.append(PointDiscount(params["points"]))

        elif discount_type == "percentagecategory":
            discount_objects.append(CategoryPercentageDiscount(params["categories"]))

        elif discount_type == "special":
            discount_objects.append(
                SpecialDiscount(
                    every_x=params["every_x"], discount_y=params["discount_y"]
                )
            )

        else:
            raise ValueError(f"Unknown discount type: {campaign['type']}")

    return discount_objects
