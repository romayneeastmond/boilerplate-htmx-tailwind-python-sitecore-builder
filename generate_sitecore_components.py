from process_form_values import process_values_props
from process_form_values import process_values_route_consoles
from process_form_values import process_values_route_fields
from process_form_values import process_values_rendering_fields
from process_form_values import process_values_rendering_fields_declarations
from process_form_values import process_values_component_parameters
from process_form_values import process_values_graphql_fields
from process_form_values import process_values_sitecore_renderings

def get_sitecore_components(name, values, hook):
    text = """
        <div class="border bg-gray-100 mt-2 relative rounded-md text-xs dark:bg-zinc-800 dark:border-zinc-700 dark:text-white">
            <h6 class="border-b border-gray-200 font-bold p-3 dark:border-zinc-700">
                Sitecore XM Cloud Component
            </h6>
            
            <button onclick="copyTextToClipboard('#response-component')" class="absolute top-2 right-2 text-gray-500 text-sm px-3 py-1 rounded dark:text-white">
                <i class="fas fa-copy"></i>
            </button>            
            
            <pre id="response-component" class="-mb-7 -mt-4 px-4">
                <code class="scrollable typescript">
import React from 'react';
import { 
    ComponentParams, ComponentRendering, DateField, Item, File, FileField,[hook_import1] Image, Link, LinkField, Text, TextField, 
    RichText, RichTextField, useSitecoreContext[hook_import2] 
} from '@sitecore-jss/sitecore-jss-nextjs';

type """ + name + """Props = {
    rendering: ComponentRendering & { params: ComponentParams };
    params: ComponentParams;
};

type ComponentContentProps = {
    id: string;
    mode?: string;
    children?: JSX.Element;[hook_component_prop]
""" + process_values_props(values) + """
};
[hook_definition]
const ComponentContent = (props: ComponentContentProps): JSX.Element => {""" + process_values_route_consoles(values) + """    
    return (
        &lt;div className='border m-4 p-4'&gt;
""" + process_values_sitecore_renderings(values) + """
        &lt;/div&gt;
    );
};

export const Default = (props: """ + name + """Props): JSX.Element => {
    const { sitecoreContext } = useSitecoreContext();
    [hook_definition_external]
    if (!props.rendering && !sitecoreContext?.route?.fields) {
        return (
            &lt;div className='text-red-600 text-sm'&gt;
                """ + name + """ rendering requires a data source.
                {/* Empty """ + name + """ Component */}
            &lt;/div&gt;
        );
    }
    
    const id = props.rendering?.uid;
    const fields = sitecoreContext?.route?.fields; 
""" + process_values_route_fields(values) + """
    // const contextFields = sitecoreContext?.route?.fields; // Used by renderings that are bound to Template fields
    // const renderingFields = props.rendering?.fields; // Used by renderings that are bound to a Datasource fields

    const renderingFields = {
""" + process_values_rendering_fields(values) + """
\t};

    if (fields) {
""" + process_values_rendering_fields_declarations(values) + """
\t}    
    
    return (
        &lt;ComponentContent
            id={id ? id : ''}
            mode={sitecoreContext.pageEditing === false ? '' : 'edit'}[hook_component_return]
""" + process_values_component_parameters(values) + """
        /&gt;
    );    
};

[hook_with_check]     
                </code>
            </pre>            
        </div>
        
        <div class="border bg-gray-100 mt-4 relative rounded-md text-xs dark:bg-zinc-800 dark:border-zinc-700 dark:text-white">            
            <h6 class="border-b border-gray-200 font-bold p-3 dark:border-zinc-700">
                GraphQL Definition
            </h6>
            
            <button onclick="copyTextToClipboard('#response-query')" class="absolute top-2 right-2 text-gray-500 text-sm px-3 py-1 rounded dark:text-white">
                <i class="fas fa-copy"></i>
            </button>             
            
            <pre id="response-query" class="-mb-7 -mt-4 px-4">
                <code class="graphql">
gql`
    query getItem($datasource: String!) {
        item(language: "en", path: $datasource) {
            url {
                path      
            },
""" + process_values_graphql_fields(values) + """
        }
    }
`;
                </code>
            </pre>            
        </div>    
    """
    
    if hook == "1":
        text_definition = """
export const getStaticProps: GetStaticComponentProps = async (rendering, layoutData) => {    
    console.log(rendering, layoutData);
    //const item = await getItemByDatasource(rendering.dataSource as string);

    //return item;
    
    return null;    
};
    """

        component_prop = """
    item: Item;"""
    
        component_return = """
            item={renderingItem as Item}"""
        
        external_definition = """const renderingItem = useComponentProps&lt;Item&gt;(props.rendering.uid);
        """
        
        text = text.replace("[hook_import1]", " GetStaticComponentProps,")
        text = text.replace("[hook_import2]", ", useComponentProps, withDatasourceCheck")
        text = text.replace("[hook_component_prop]", component_prop)
        text = text.replace("[hook_definition_external]", external_definition)
        text = text.replace("[hook_definition]", text_definition)
        text = text.replace("[hook_component_return]", component_return)
        text = text.replace("[hook_with_check]", "export default withDatasourceCheck()&lt;" + name + "Props&gt;(Default);")
    else:
        text = text.replace("[hook_import1]", "")
        text = text.replace("[hook_import2]", "")
        text = text.replace("[hook_component_prop]", "")
        text = text.replace("[hook_definition_external]", "")
        text = text.replace("[hook_definition]", "")
        text = text.replace("[hook_component_return]", "")
        text = text.replace("[hook_with_check]", "")
    
    return text        