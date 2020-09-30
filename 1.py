import shapefile
import pprint
from shapely.geometry import Polygon, Point
from shapely.validation import make_valid
import math

sf_pc4 = shapefile.Reader("shape_files/PC4")
myshp_pc4 = open("shape_files/PC4.shp", "rb")
mydbf_pc4 = open("shape_files/PC4.dbf", "rb")
r_pc4 = shapefile.Reader(shp=myshp_pc4, dbf=mydbf_pc4)

sf_traffic = shapefile.Reader("shape_files/traffic_model_zones")
myshp_traffic = open("shape_files/traffic_model_zones.shp", "rb")
mydbf_traffic = open("shape_files/traffic_model_zones.dbf", "rb")
r_traffic = shapefile.Reader(shp=myshp_traffic, dbf=mydbf_traffic)

filename = "areanr_PC4.csv" #output.txt" #
my_file = open(filename, "w", encoding="utf8")
my_file.write("ObjectID,Shape,PC4,Areanr\n")


shapes_pc4 = sf_pc4.shapes()
shapes_traffic = sf_traffic.shapes()

print(str(len(shapes_pc4)))
print(str(len(shapes_traffic)))

fields = sf_traffic.fields[1:] 
field_names = [field[0] for field in fields] 
pprint.pprint(field_names)

c = 0
c_2 = 0
for i_1 in range(len(shapes_traffic)):
    # print(str(i_1))
    bbox_1 = shapes_traffic[i_1].bbox
    max_area = 0
    max_id = -1
    total_area = 0
    poly_1 = make_valid(Polygon(shapes_traffic[i_1].points))

    for i_2 in range(len(shapes_pc4)):
        bbox_2 = shapes_pc4[i_2].bbox
        # if Polygon(outline_1).intersects(Polygon(outline_2)):
        if ((bbox_2[0] - bbox_1[0]) * (bbox_2[2] - bbox_1[0]) < 0 or (bbox_2[0] - bbox_1[2]) * (bbox_2[2] - bbox_1[2]) < 0) and ((bbox_2[1] - bbox_1[1] ) * (bbox_2[3] - bbox_1[1]) < 0 or (bbox_2[1] - bbox_1[3]) * (bbox_2[3] - bbox_1[3]) < 0) or ((bbox_1[0] - bbox_2[0]) * (bbox_1[2] - bbox_2[0]) < 0 or (bbox_2[0] - bbox_2[2]) * (bbox_1[2] - bbox_2[2]) < 0) and ((bbox_1[1] - bbox_2[1] ) * (bbox_1[3] - bbox_2[1]) < 0 or (bbox_1[1] - bbox_2[3]) * (bbox_1[3] - bbox_2[3]) < 0):
            # print("i1 = " + str(i_1) + "  i2 = " + str(i_2))
            poly_2 = make_valid(Polygon(shapes_pc4[i_2].points))
            if not poly_2.is_valid:
                poly_2 = make_valid(poly_2)
            
            if not poly_1.intersects(poly_2):
                min_ang = math.pi
                max_ang = - math.pi
                pre_ang = 100 * math.pi                
                for pp in shapes_pc4[i_2].points:
                    p0 = shapes_traffic[i_1].points[0]
                    ang =  math.atan2(pp[1]-p0[1], pp[0]-p0[0])
                    # if i_2 == 335 : print("pre = " + str(pre_ang) + " ang = " + str(ang))
                    if pre_ang < 99 * math.pi and math.fabs(ang - pre_ang) > math.pi:
                        if ang < pre_ang: 
                            ang += 2 * math.pi
                            # if i_2 == 335 : print("ok " + str(ang))
                        elif ang > pre_ang: ang -= 2 * math.pi
                    # if i_2 == 335 : print("ang = " + str(ang))
                    if ang > max_ang : max_ang = ang
                    if ang < min_ang : min_ang = ang
                    if max_ang - min_ang > math.pi * 1.8 : break
                    pre_ang = ang
                # print("1  -   " + str(max_ang) + "  " + str(min_ang))
                if max_ang - min_ang > math.pi * 1.8 :
                    intersect_area = poly_1.area
                else:
                    min_ang = math.pi
                    max_ang = - math.pi
                    pre_ang = 100 * math.pi 
                    for pp in shapes_traffic[i_1].points:
                        p0 = shapes_pc4[i_2].points[0]
                        ang =  math.atan2(pp[1]-p0[1], pp[0]-p0[0])
                        if pre_ang < 99 * math.pi and math.fabs(ang - pre_ang) > math.pi:
                            if ang < pre_ang: 
                                ang += 2 * math.pi
                                # if i_2 == 335 : print("ok " + str(ang))
                            elif ang > pre_ang: ang -= 2 * math.pi
                        # if i_2 == 335 : print("ang = " + str(ang))
                        if ang > max_ang : max_ang = ang
                        if ang < min_ang : min_ang = ang
                        if max_ang - min_ang > math.pi * 1.8 : break
                        pre_ang = ang
                    # print("2  -   " + str(max_ang) + "  " + str(min_ang))
                    if max_ang - min_ang > math.pi * 1.8 :
                        intersect_area = poly_2.area
                    else:
                        intersect_area = 0
            else:                
                c += 1
                intersect_area = poly_1.intersection(poly_2).area
            
            if intersect_area > max_area:
                max_area = intersect_area
                max_id = i_2
            total_area += intersect_area
            if total_area + max_area >= poly_1.area: break
            
    print(str(i_1) + ", Polygon, " + str(max_id) + "   " + str(sf_pc4.record(max_id)['PC4']) + ", " + str(int(sf_traffic.record(i_1)['AREANR'])) + "\n")
    rec = sf_pc4.record(3)
    my_file.write(str(i_1) + ",Polygon," + str(sf_pc4.record(max_id)['PC4']) + "," + str(int(sf_traffic.record(i_1)['AREANR'])) + "\n")
my_file.close()
