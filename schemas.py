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


class BlindClassificationWine(Schema):
    wine_id = fields.Int(validate=validate.Range(-10000, 10000))
    
    for field_name, (min_value, max_value) in features_fields_ranges.items():
        vars()[field_name] = fields.Float(
            required=True,
            validate=validate.Range(min=min_value, max=max_value)
        )
        
class WineClassified(BlindClassificationWine):
    quality_regression_pred = fields.Float(
        validate=validate.Range(0,11)
        )
    
    recommendation = fields.Str(
        validate=validate.Length(max=100)
        )
    
    bin_pred = fields.Int(
        validate=validate.Range(0, 1)
        )
    
    quality = fields.Int(
        validate=validate.Range(0, 10)
        )
    
    bin_quality = fields.Int(
        validate=validate.Range(0, 1)
        )
    
    
    
    
    
    
    
    
