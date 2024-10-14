import argparse
import math
from statistics import mean

def phred_to_probability(phred_score):
    return 10 ** (-phred_score / 10)

def probability_to_phred(error_probability):
    return -10 * math.log10(error_probability)

def decode(qual_char):
    return ord(qual_char) - 33

def calculate_gc_content(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100 if len(sequence) > 0 else 0

def calculate_mean_quality(fastq_file, output_file):
    with open(fastq_file, 'r') as file, open(output_file, 'w') as out:
        out.write("Identifiers\tQuality\tLength\tGC_content\n")

        while True:
            header = file.readline().strip()    # Read the header line (unique identifier)
            if not header:
                break
            sequence = file.readline().strip() # Read the sequence line
            plus = file.readline().strip()     # Read the '+' line
            quality = file.readline().strip()  # Read the quality line

            # Extract the unique read identifier (up to the first whitespace)
            read_id = header.split()[0].lstrip('@')
            
            # Calculate error probabilities for the quality scores
            error_probabilities = [phred_to_probability(decode(q)) for q in quality]
            mean_error_probability = mean(error_probabilities)
            mean_quality_score = probability_to_phred(mean_error_probability)
            
            # Calculate read length and GC content
            read_length = len(sequence)
            gc_content = calculate_gc_content(sequence)

            # Write the result to the output file
            out.write(f"{read_id}\t{mean_quality_score:.2f}\t{read_length}\t{gc_content:.2f}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate mean quality, length, and GC content per read from a FASTQ file")
    parser.add_argument("--input", required=True, help="Input FASTQ file")
    parser.add_argument("--output", required=True, help="Output file to write quality scores, length, and GC content")

    args = parser.parse_args()
    calculate_mean_quality(args.input, args.output)