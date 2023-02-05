## Fist, just download the compressed file "HT_Detection.tar.gz" to your folder, the folder must contain the following files:
1. ***CHIP.v*** : The gate level netlist of the circuit
2. ***process.v*** : The process file which you use to synthesis the RTL

## Then untar the compressed file "HT_Detection.tar.gz" with the following command:

    tar -zxvf HT_Detection.tar.gz
    
## After untar the file, then use the following command:

    sh Feature_Extract.sh
    
### Then the result will be done automatically. You can check whether your circuit is secure or not.


## The folowing are the usage of each files:

- cp.sh:複製製程檔，以避免原製程檔受到更動。
- Process_Editor.sh:對製程檔進行結構的修正，以利進行邏輯閘的提取及分析。
- Gate_Analysizer.sh:將製程檔中邏輯閘的input、output、inout提取出來(Gate_Analysizer.cpp)。
- CHIP_Edit.sh:對硬體木馬之邏輯閘層級網表進行結構的修正，以利進行分析(CHIP_Edit.cpp)。
- Gate_Level_Analysis.sh:對硬體木馬之邏輯閘層級網表進行特徵(feature)的文字分析，產出 CHIP_Feather_File.csv之分析檔(Gate_Level_Analysis.cpp)。
- Feature_Extract.sh:整合以上所有動作，一次性完成。

※ To be done : not to untar the files in the operating folder
