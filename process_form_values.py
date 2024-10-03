def process_values_component_parameters(values):
    parameters = ""
    
    if not values.strip():
        return parameters
    
    lines = values.strip().split('\n')
    
    for line in lines:
        items = [item.strip() for item in line.split(',')]
        
        parameters += "\t\t\t" + items[1] + "={renderingFields." + items[1] + "}\n"
        
    return parameters[:-1]

def process_values_graphql_fields(values):
    fields = ""
    
    if not values.strip():
        return fields
    
    lines = values.strip().split('\n')
    
    for line in lines:
        items = [item.strip() for item in line.split(',')]
        
        fields += "\t\t\t" + items[1] + ": field(name: \"" + items[2] + "\") {\n\t\t\t\tvalue\n\t\t\t},\n"
        
    return fields[:-2]

def process_values_props(values):
    props = ""
    
    if not values.strip():
        return props
    
    lines = values.strip().split('\n')
    
    for line in lines:
        items = [item.strip() for item in line.split(',')]
        
        props += "\t" + items[1] + ": " + items[0] + ";\n"
    
    return props[:-1]

def process_values_rendering_fields(values):
    rendering_fields = ""
    
    if not values.strip():
        return rendering_fields
    
    lines = values.strip().split('\n')
    
    for line in lines:
        items = [item.strip() for item in line.split(',')]
        
        rendering_fields += "\t\t" + items[1] + ": {},\n"
        
    return rendering_fields[:-2]

def process_values_rendering_fields_declarations(values):
    declarations = ""
    
    if not values.strip():
        return declarations
    
    lines = values.strip().split('\n')
    
    for line in lines:
        items = [item.strip() for item in line.split(',')]
        
        declarations += "\t\trenderingFields." + items[1] + " = fields['" + items[2] + "'];\n"
        
    return declarations[:-1]

def process_values_sitecore_renderings(values):
    renderings = ""
    
    if not values.strip():
        return renderings
    
    lines = values.strip().split('\n')
    
    for line in lines:
        items = [item.strip() for item in line.split(',')]
        
        if (items[3].strip().lower() == "text"):        
            renderings += "\t\t\t&lt;Text field={props." + items[1] + " as TextField} /&gt;\n\n"            
        elif (items[3].strip().lower() == "richtext"):        
            renderings += "\t\t\t&lt;RichText field={props." + items[1] + " as RichTextField} /&gt;\n\n"            
        elif (items[3].strip().lower() == "link"):        
            renderings += "\t\t\t&lt;Link field={props." + items[1] + "} /&gt;\n\n"        
        elif (items[3].strip().lower() == "image"):        
            renderings += "\t\t\t&lt;Image field={props." + items[1] + "} /&gt;\n\n"     
        elif (items[3].strip().lower() == "date"):        
            renderings += "\t\t\t&lt;DateField field={props." + items[1] + "} /&gt;\n\n"          
        elif (items[3].strip().lower() == "file"):        
            renderings += "\t\t\t&lt;File field={props." + items[1] + " as FileField} target='_blank'&gt\n\t\t\t\tDownload\n\t\t\t&lt;/File&gt;\n\n"                             
        elif (items[3].strip().lower() == "none"):        
            renderings += "\t\t\t{props." + items[1] + "}\n\n"
        else:
            renderings += "\t\t\t{props." + items[1] + "}\n\n"
            
    return renderings[:-2]