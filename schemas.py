from marshmallow import Schema, fields, validate, ValidationError

# Mínimos e máximos estimado de features (db[feature].min()*0.8, db[feature].max()*1.2)
features_fields_ranges = {
    'fixed_acidity': (3.68, 19.08),
    'volatile_acidity': (0.10, 1.90),
    'citric_acid': (0.00, 1.20),
    'residual_sugar': (0.72, 18.60),
    'chlorides': (0.01, 0.73),
    'free_sulfur_dioxide': (0.80, 86.40),
    'total_sulfur_dioxide': (4.80, 346.80),
    'density': (0.79, 1.20),
    'pH': (2.19, 4.01),
    'sulphates': (0.26, 2.40),
    'alcohol': (6.72, 17.88)
    }

binary_integer_err = "O valor inteiro deve ser 0 (ruim) ou 1 (bom)."
ten_integer_err = "O valor inteiro deve estar entre 0 e 10."
ten_mil_integer_err = "O valor inteiro deve estar entre 0 e 10.000."
refuse_rec = 'Cilada Bino! Não recomendo este vinho.'
neutral_rec = 'Glória Pires: Não sei opinar/O vinho pode ser bom, ou não, segundo os critérios adotados'

class BlindClassificationWine(Schema):
    wine_id = fields.Int(validate=validate.Range(-10000, 10000))
    for field_name, (min_value, max_value) in features_fields_ranges.items():
        vars()[field_name] = fields.Float(
            required=True,
            validate=validate.Range(
                min=min_value, 
                max=max_value,
                error=f'O valor deve uma variável "Float" dentro do intervalo: {features_fields_ranges[field_name]}'
            )
        )
        
###########################################################################################
        
class ClassifierPredictionWineOutput(Schema):
    bin_quality = fields.Int(                # Para caso de comparação
        validate=validate.OneOf([0, 1], error=binary_integer_err)
    )
    wine_id = fields.Int(                    # Passe um id se quiser e ele sera mantido
        validate=validate.Range(-10000, 10000, error=ten_mil_integer_err)
    )
    bin_pred = fields.Int(
        required=True,
        validate=validate.OneOf([1, 0], error=binary_integer_err)
    )   
    

class ClassifierPredictionWineInput(BlindClassificationWine):
    bin_quality = fields.Int(                # Para caso de comparação
        validate=validate.OneOf([0, 1], error=binary_integer_err)
    )
    wine_id = fields.Int(                    # Passe um id se quiser e ele sera mantido
        validate=validate.Range(-10000, 10000, error=ten_mil_integer_err)
    )
    
###########################################################################################

class RegressPredictionOutput(Schema):
    quality = fields.Int(            # Para caso de comparação
        validate=validate.Range(0, 10, error=ten_integer_err)
    )
    wine_id = fields.Int(                
        validate=validate.Range(-10000, 10000, error=ten_mil_integer_err)
    )
    quality_regression_pred = fields.Float(
        required=True,
        validate=validate.Range(0,10, error='Valor fora dos limites possíveis (0 a 10).')
    )
    
class RegressPredictionInput(BlindClassificationWine):
    quality = fields.Int(            # Para caso de comparação
        validate=validate.Range(0, 10, error=ten_integer_err)
    )
    wine_id = fields.Int(                
        validate=validate.Range(-10000, 10000, error=ten_mil_integer_err)
    )
    
 ###########################################################################################   
    
class RecommendationOutput(Schema):
    bin_quality = fields.Int(                # Para caso de comparação
        validate=validate.OneOf([0, 1], error=binary_integer_err)
    )

    wine_id = fields.Int(                
        validate=validate.Range(-10000, 10000, error=ten_mil_integer_err)
    )
    
    recommendation= fields.Str(
        required=True,
        validate=validate.OneOf([refuse_rec,
                                neutral_rec],
                                error='Recomendação fora do escopo.')
    )    
    
class RecommendationInput(BlindClassificationWine):
    bin_quality = fields.Int(                # Para caso de comparação
        validate=validate.OneOf([0, 1], error=binary_integer_err)
    )

    wine_id = fields.Int(                
        validate=validate.Range(-10000, 10000, error=ten_mil_integer_err)
    )
    
