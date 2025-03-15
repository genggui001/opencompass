mkdir -p ./datasources/data
for folder in ./cibench_template/*;
do
    if [ -d $folder/data ]; then
        cp -r $folder/data/* ./datasources/data/;
        echo 'Template data prepare finished.'
    fi
done
for folder in ./cibench_generation/*;
do
    if [ -d $folder/data ]; then
        cp -r $folder/data/* ./datasources/data/;
        echo 'Generation data prepare finished.'
    fi
done
