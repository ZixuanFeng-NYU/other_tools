import os
import bz2
import multiprocessing

def decompress_file(file_path):
    with open(file_path,'rb')as input_file:
        with open(os.path.splitext(file_path)[0],'wb') as output_file:
            decompressor = bz2.BZ2Decompressor()
            for data in iter(lambda: input_file.read(100*1024*1024),b''):
                output_file.write(decompressor.decompress(data))

if __name__=='__main__':
    file_paths = ['Enamine_REAL_HAC_6_21_420M_CXSMILES.cxsmiles.bz2','Enamine_REAL_HAC_22_23_471M_CXSMILES.cxsmiles.bz2','Enamine_REAL_HAC_24_394M_CXSMILES.cxsmiles.bz2','Enamine_REAL_HAC_25_557M_CXSMILES.cxsmiles.bz2','Enamine_REAL_HAC_26_833M_Part_1_CXSMILES.cxsmiles.bz2','Enamine_REAL_HAC_26_833M_Part_2_CXSMILES.cxsmiles.bz2','Enamine_REAL_HAC_27_1.1B_Part_1_CXSMILES.cxsmiles.bz2','Enamine_REAL_HAC_27_1.1B_Part_2_CXSMILES.cxsmiles.bz2','Enamine_REAL_HAC_28_1.2B_Part_1_CXSMILES.cxsmiles.bz2','Enamine_REAL_HAC_28_1.2B_Part_2_CXSMILES.cxsmiles.bz2','Enamine_REAL_HAC_29_38_988M_Part_1_CXSMILES.cxsmiles.bz2','Enamine_REAL_HAC_29_38_988M_Part_2_CXSMILES.cxsmiles.bz2']
    pool = multiprocessing.Pool()
    pool.map(decompress_file,file_paths)
    pool.close()
    pool.join()
