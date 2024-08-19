__all__ = [
    "DAO",
    "dao"
]
class DAO:
    def __request_sql(self, request):
        # TODO: To be implemented
        raise NotImplementedError
    
    def __get_objects_in_table(self, table_name: str, filter_params=[]):
        get_from_table_request = f"SELECT * FROM {table_name}"
        
        if filter_params:
            filter_request = " ".join(["WHERE", *filter_params])
        request = " ".join([get_from_table_request, filter_request])
        return self.__request_sql(request)


    def get_product(self, product_type_id: int, product_id: int):
        product = self.__get_objects_in_table('product_type', f'id={product_type_id}')
        assert len(product) != 0, f"No product type has been found for id {product_type_id}"
        assert len(product) == 1, f"Several products have been found for primary key id = {product_type_id}"
        interpreted_object = product[0].interpret_object()
        table_name = self.__get_table_from_name(interpreted_object.__class__.__name__)
        product_objects = self.__get_objects_in_table(interpreted_object.__class__.__name__)
        return self.__get_objects_in_table(table_name, f'{table_name}_id={product_type_id}')[0].interpret_object()

    def __get_table_from_name(class_name: str):
        table_name = []
        for i, letter in enumerate(class_name[:-4]): # Remove Data particule
            if letter.isupper() and i != 0:
                table_name.append('_')
        return "".join(table_name).lower()

dao = DAO()