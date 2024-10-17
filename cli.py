import click
from faker_data_generator import load_schema, generate_fake_data
import json

@click.command()
@click.argument('schema_file', type=click.Path(exists=True))
@click.option('--num-records',
              default=10,
              help='Number of fake records to generate.')
@click.option('--output-file',
              type=click.Path(),
              help='Optional output file to save the generated data.')
def generate(schema_file, num_records, output_file):
    """
    Generate fake data based on a given SCHEMA_FILE.
    
    SCHEMA_FILE is a path to a JSON or YAML schema file 
    that defines the structure of the data.
    """
    try:
        schema = load_schema(schema_file)
        data = generate_fake_data(schema, num_records)

        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            click.echo(f"Fake data generated and saved to {output_file}")
        else:
            for record in data:
                click.echo(record)
    except ValueError as e:
        click.echo(f"Error: {e}")

if __name__ == '__main__':
    generate()