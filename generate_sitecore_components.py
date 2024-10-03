from process_form_values import process_values_props
from process_form_values import process_values_rendering_fields
from process_form_values import process_values_rendering_fields_declarations
from process_form_values import process_values_component_parameters
from process_form_values import process_values_graphql_fields
from process_form_values import process_values_sitecore_renderings

def get_sitecore_components(name, values):
    return """
        <div class="border bg-gray-100 mt-2 rounded-md text-xs dark:bg-zinc-800 dark:border-zinc-700 dark:text-white">
            <h6 class="border-b border-gray-200 font-bold p-3 dark:border-zinc-700">
                Sitecore XM Cloud Component
            </h6>            
            
            <pre id="response-component" class="-mb-7 -mt-4 px-4">
                <code class="typescript">
import React from 'react';
import { 
    ComponentParams, ComponentRendering, DateField, File, FileField, Image, Link, LinkField, Text, TextField, 
    RichText, RichTextField, useSitecoreContext 
} from '@sitecore-jss/sitecore-jss-nextjs';

type """ + name + """Props = {
    rendering: ComponentRendering & { params: ComponentParams };
    params: ComponentParams;
}

type ComponentContentProps = {
    id: string;
    mode?: string;
    children?: JSX.Element;
""" + process_values_props(values) + """
}

const ComponentContent = (props: ComponentContentProps): JSX.Element => {
    return (
        &lt;div className='border m-4 p-4'&gt;
""" + process_values_sitecore_renderings(values) + """
        &lt;/div&gt;
    );
};

export const Default = (props: """ + name + """Props): JSX.Element => {
    const { sitecoreContext } = useSitecoreContext();

    if (!props.rendering && !sitecoreContext?.route?.fields?.Content) {
        return (
            &lt;div className='text-red-600 text-sm'&gt;
                """ + name + """ rendering requires a data source.
                {/* Empty """ + name + """ Component */}
            &lt;/div&gt;
        );
    }
    
    const id = props.rendering?.uid;
    const fields = props.rendering?.fields;

    const renderingFields = {
""" + process_values_rendering_fields(values) + """
\t};

    if (fields) {
""" + process_values_rendering_fields_declarations(values) + """
\t}    
    
    return (
        &lt;ComponentContent
            id={id ? id : ''}
            mode={sitecoreContext.pageEditing === false ? '' : 'edit'}
""" + process_values_component_parameters(values) + """
        /&gt;
    );    
};     
                </code>
            </pre>            
        </div>
        
        <div class="border bg-gray-100 mt-4 rounded-md text-xs dark:bg-zinc-800 dark:border-zinc-700 dark:text-white">            
            <h6 class="border-b border-gray-200 font-bold p-3 dark:border-zinc-700">
                GraphQL Definition
            </h6>
            
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